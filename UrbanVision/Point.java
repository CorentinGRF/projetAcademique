
import java.awt.Color;

public class Point {
	
	private float x;
	private float y;
	private float z;
	private float nx;
	private float ny;
	private float nz;
	private int r; 
	private int v;
	private int b;
	private int num;
	
	public Point(){
		this(0,0,0,0,0,0,0,0,0,0);
	}

	public Point(float x,float y,float z,float nx,float ny,float nz, int r, int v, int b, int num){
		this.x = x;
		this.y = y;
		this.z = z;
		this.nx = nx;
		this.ny = ny;
		this.nz = nz;
		this.r = r;
		this.v = v;
		this.b = b;
		this.num = num;
	}
	
	public Point(float x,float y,float z, int r, int v, int b, int num){
		this(x,y,z,0,0,0,r,v,b,num);
	}
	
	public float getX(){
		return this.x;
	}
	
	public float getY(){
		return this.y;
	}
	
	public float getZ(){
		return this.z;
	}
	
	public float getNX(){
		return this.nx;
	}
	
	public float getNY(){
		return this.ny;
	}
	
	public float getNZ(){
		return this.nz;
	}
	
	public int getR(){
		return this.r;
	}
	
	public int getV(){
		return this.v;
	}
	
	public int getB(){
		return this.b;
	}
	
	public int getNum(){
		return this.num;
	}
	
	public Color getColor(){
		return new Color(this.r,this.v,this.b);
	}
	
	@Override
	public String toString(){
		return ("Point(x:"+x+",y:"+y+",z:"+z+",nx:"+nx+",ny:"+ny+",nz:"+nz+",r:"+r+",v:"+v+",b:"+b+")");
	}
}