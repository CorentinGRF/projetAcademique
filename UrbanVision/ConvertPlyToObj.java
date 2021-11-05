
import java.io.File;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.awt.Color;
import java.util.HashMap;
import java.io.FileWriter;
import java.awt.image.BufferedImage;
import java.awt.Graphics2D;
import javax.imageio.ImageIO;
import java.awt.Rectangle;
import java.awt.geom.Point2D;

public class ConvertPlyToObj {
	
	HashMap<Color,Integer> colormap;
	Point[] pointlist;
	Face[] facelist;
    
	private String inputFile;
	private String outputFile;
	
	public static int CASE_SIZE = 8;
	public static String RESULT_DIRECTORY = "result/";
	public ConvertPlyToObj(String inputName,String outputName){
		this.inputFile = inputName;
		this.outputFile = outputName;
		this.colormap = new HashMap<Color,Integer>();
	}
	
	//Chargement des donnée du ply
	public int loadData(){
		
		Pattern elementPattern = Pattern.compile("element\\s(vertex|face)\\s(\\d+)");
		Pattern vertexPattern = Pattern.compile("(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(-?\\d+(?:\\.\\d+)?(?:e-?\\d+)?)\\s(\\d+)\\s(\\d+)\\s(\\d+)\\s(\\d+)\\s*");
		Pattern facePattern = Pattern.compile("(\\d+)\\s(\\d+)\\s(\\d+)\\s(\\d+)\\s*");
		
		
		File    file = new File(this.inputFile);
		Scanner scanner;
		try{
		    scanner     = new Scanner(file);
		} catch (Exception e){
			System.out.println(e);
			return -1;
		}
		
		scanner.nextLine(); //ply
		scanner.nextLine(); //format
		int nbFace = 0;
		int nbVertex = 0;
		
		String nextLine;
	    Matcher m;
		//recherche le nombre de point et le nombre de face dans l'entête
		while(!(nextLine = scanner.nextLine()).startsWith("end_header")) {
			if((m = elementPattern.matcher(nextLine)).matches()){
				switch(m.group(1)){
					case "vertex":
					nbVertex = Integer.parseInt(m.group(2));
					System.out.println("NbrVertex : "+nbVertex);
					break;
					case "face":
					nbFace = Integer.parseInt(m.group(2));
					System.out.println("NbrFace : "+nbFace);
					break;
					default:
				}
			}
		}
		
		this.pointlist = new Point[nbVertex];
		this.facelist = new Face[nbFace];
		
		//charge les points
		for(int i = 0 ; i < nbVertex ; i++){
			nextLine = scanner.nextLine();
			m = vertexPattern.matcher(nextLine);
			
			if(m.matches()){
				this.pointlist[i] = new Point(
				Float.parseFloat(m.group(1)),
				Float.parseFloat(m.group(2)),
				Float.parseFloat(m.group(3)),
				Float.parseFloat(m.group(4)),
				Float.parseFloat(m.group(5)),
				Float.parseFloat(m.group(6)),
				Integer.parseInt(m.group(7)),
				Integer.parseInt(m.group(8)),
				Integer.parseInt(m.group(9)),
				i+1
				);
			} else {
				this.pointlist[i] = new Point();
			}
		}
		
		//charge les face
		for(int i = 0,indice = 0; i < nbFace ; i++){
			nextLine = scanner.nextLine();
			m = facePattern.matcher(nextLine);
			this.facelist[i] = new Face();
			
			//Ajoue des points dans une face
			if(m.matches()){
				this.facelist[i].addPoint(this.pointlist[Integer.parseInt(m.group(2))]);
				this.facelist[i].addPoint(this.pointlist[Integer.parseInt(m.group(3))]);
				this.facelist[i].addPoint(this.pointlist[Integer.parseInt(m.group(4))]);
			}
			//Calcule de la couleur de la face à partir de la couleur des points
			this.facelist[i].calculColor();
			//Ajoue de la couleur de la face dans la Hashmap pour la création de la texture
			Color c = this.facelist[i].getColor();
			if(!this.colormap.containsKey(c)){
				this.colormap.put(c,indice);
				indice++;
			}
		}
		System.out.println("NbrColor : "+colormap.keySet().size());
		return 0;
	}
	
	public int createTex(){
		
		//Calcule de la taille de la texture en pixel (la texture est toujour carré)
		int texDim = (int)Math.round(Math.sqrt(colormap.keySet().size())+0.5f)*CASE_SIZE;
		
		BufferedImage tex = new BufferedImage(texDim,texDim,BufferedImage.TYPE_INT_RGB);
		Graphics2D g = 	tex.createGraphics();
		
		int nb = 0;
		//Création de la texture
		for(Color tc : this.colormap.keySet()){
			
			g.setPaint(tc);
			g.fill(new Rectangle((this.colormap.get(tc)*CASE_SIZE)%texDim,((this.colormap.get(tc)*CASE_SIZE)/texDim)*8,CASE_SIZE,CASE_SIZE ));
			
			nb++;			
		}
		
		//Sauvegarde de la texture
		try {
			File outputfile = new File(RESULT_DIRECTORY+this.outputFile+"_tex.png");
			ImageIO.write(tex, "png", outputfile);
		} catch (Exception e) {
			System.out.println(e);
			return -1;
		}	
		
		//Ajoue de sa cordonnée de texture à chaque point 
		for(Face f : this.facelist){
			int x = (this.colormap.get(f.getColor())*CASE_SIZE)%texDim;
			int y = texDim-((this.colormap.get(f.getColor())*CASE_SIZE)/texDim)*8-8;
			
			f.addTexPoint(new Point2D.Float((x+1f)/texDim,(y+1f)/texDim));
			f.addTexPoint(new Point2D.Float((x+CASE_SIZE-1f)/texDim,(y+1f)/texDim));
			f.addTexPoint(new Point2D.Float((x+1f)/texDim,(y+CASE_SIZE-1f)/texDim));
		}
		return 0;
	}
		
	public int writeObj(){
		//Création du OBJ 
		try {
			// retrieve image
			FileWriter fw = new FileWriter( RESULT_DIRECTORY+this.outputFile+".obj");
		    //Création du matériaux 
			fw.write("mtllib ./"+this.outputFile+".obj.mtl\r\n");
			//Création des point/vecteur normal
			for(int i = 0 ; i < pointlist.length ; i++){
				fw.write("vn "+this.pointlist[i].getNX()+" "+this.pointlist[i].getNY()+" "+this.pointlist[i].getNZ()+"\r\n");
				fw.write("v "+this.pointlist[i].getX()+" "+this.pointlist[i].getY()+" "+this.pointlist[i].getZ()+"\r\n");
			}	
			fw.write("usemtl material_0\r\n");	
			int counter = 1;
			//Création des face/coordonée de texture
			for(int i = 0 ; i < facelist.length ; i++){
				for(Point2D p : this.facelist[i].getTexPointList()){
					fw.write("vt "+p.getX()+" "+p.getY()+"\r\n");
				}		
				String str = "f";
				for(Point p : this.facelist[i].getPointList()){
					str += " "+p.getNum()+"/"+counter+"/"+p.getNum();
					counter++;
				}			
				fw.write(str+"\r\n");	
			}
			fw.close();
		} catch (Exception e) {
			System.out.println(e);
			return -1;
		}	
		return 0;
	}
	
	public int writemtl(){
		//Création du MLT 
		try {
			FileWriter fw = new FileWriter( RESULT_DIRECTORY+this.outputFile+".obj.mtl");
			fw.write("newmtl material_0\r\n");
			fw.write("Ka 1.000000 1.000000 1.000000\r\n");
			fw.write("Kd 1.000000 1.000000 1.000000\r\n");
			fw.write("Ks 1.000000 1.000000 1.000000\r\n");
			fw.write("Tr 1.000000\r\n");
			fw.write("illum 2\r\n");
			fw.write("Ns 0.000000\r\n");
			fw.write("map_Kd "+this.outputFile+"_tex.png\r\n");
			fw.close();
		} catch (Exception e) {
			System.out.println(e);
			return -1;
		}	
		return 0;
	}
}