
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

public class Main {
	
	public static int CASE_SIZE = 8;
	
	public static void main(String[] args){
		//Argument 1 : nom du fichier en entr�e, Argument 2 : nom du fichier de sortie sans l'extension
		//Attention par default les fichier sont sauvegarder dans le dossier result
		if(args.length < 2){
			System.out.println("Nombre d'argument invalide");
			return;
		}
		
		String inputName = args[0];
		String outputName = args[1];
		
		ConvertPlyToObj converter = new ConvertPlyToObj(inputName,outputName);	
		
		System.out.println("Chargement des donn�es");
		if(converter.loadData() != 0){
			return;
		}
		System.out.println("Cr�ation de la texture");
		if(converter.createTex() != 0){
			return;
		}
		System.out.println("Cr�ation du .obj");
		if(converter.writeObj() != 0){
			return;
		}
		System.out.println("Cr�ation du .obj.mlt");
		if(converter.writemtl() != 0){
			return;
		}
		
	}
}