import java.util.ArrayList;
import java.awt.Color;
import java.awt.geom.Point2D;

public class Face {
	
	private ArrayList<Point> pointList;
	private ArrayList<Point2D> texPointList;
	private int r; 
	private int v;
	private int b;
	public static int ARR = 5;
	
	public Face(){
		this.pointList = new ArrayList();
		this.texPointList = new ArrayList();
		this.r = 0;
		this.v = 0;
		this.b = 0;
	}
	
	public void addPoint(Point p){
		pointList.add(p);
	}
	
	public void addTexPoint(Point2D p){
		texPointList.add(p);
	}
	
	//Calcule la couleur de la face en fesant la moyenne des couleurs des points 
	public void calculColor(){
		int tr = 0;
		int tv = 0;
		int tb = 0;
		for(Point p : pointList){
			tr += p.getR();
			tv += p.getV();
			tb += p.getB();
		}
		this.r = tr/pointList.size();
		this.v = tv/pointList.size();
		this.b = tb/pointList.size();
	    //Arondie de la couleur pour limité la taille du fichier texture 
		this.r -= r%ARR;
		this.v -= v%ARR;
		this.b -= b%ARR;
	}

	public ArrayList<Point> getPointList(){
		return this.pointList;
	}
	
	public ArrayList<Point2D> getTexPointList(){
		return this.texPointList;
	}
	
	public Color getColor(){
		return new Color(this.r,this.v,this.b);
	}
	
	@Override
	public String toString(){
		String s = "Face(\n";
		s += "Color(r:"+this.r+",v:"+this.v+",b:"+this.b+")\n";
		for(Point p : pointList)
			s += "Point(x:"+p.getX()+",y:"+p.getY()+",z:"+p.getZ()+",nx:"+p.getNX()+",ny:"+p.getNY()+",nz:"+p.getNZ()+",r:"+p.getR()+",v:"+p.getV()+",b:"+p.getB()+")\n";
		s+=")";
		return s;
	}
}