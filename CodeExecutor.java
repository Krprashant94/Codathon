import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class CodeExecutor extends Thread {
	public  boolean tle=true;
	private String programName;
	private Runtime rt;
	private Process p;
	public String result="";
	public String errorMssg="";
	public boolean error = false;
	public String ext ="";
	public String input = "";
	public double exeTime = 0.0;
	public CodeExecutor(String programName,String ext,String input){
		this.programName=programName;
		rt=Runtime.getRuntime();
		this.ext = ext;
		this.input = input;
	}
	public void run(){
		try{
			if(ext.equals("java")){
				runJava();
			}
			else if(ext.equals("c")){
				runC();
			}
			else if(ext.equals("cpp")){
				runCPP();
			}
			else if(ext.equals("py2")){
				runPython2();
			}
			else if(ext.equals("py3")){
				runPython3();	
			}
			
		}
		catch(Exception e){
			System.out.println(e.fillInStackTrace());
		}
	}
	public void runJava()throws Exception{
		long t1=System.currentTimeMillis();
		p=rt.exec("java -cp "+programName);
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
		//bw.write(2);
		//System.out.println(input);
		bw.write(input+"\n");
		bw.flush();
		//System.out.println("working");
		p.waitFor();
		
		
		BufferedReader br;
		if(p.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(p.getErrorStream()));
			error = true;
			
		}
		else{
			br=new BufferedReader(new InputStreamReader(p.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			result+=s+"\n";
			//System.out.println(s);
		}
		long t2=System.currentTimeMillis();
		tle=false;
		exeTime = (t2-t1)/(double)1000;
		//System.out.println("Executed in "+exeTime);
	}
	public void runC()throws Exception{
		long t1=System.currentTimeMillis();
		p=rt.exec(programName);
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
		//bw.write(2);
		//System.out.println(input);
		bw.write(input+"\n");
		bw.flush();
		//System.out.println("working");
		p.waitFor();
		
		
		bw.append(input);
		BufferedReader br;
		if(p.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(p.getErrorStream()));
			error = true;
			
		}
		else{
			br=new BufferedReader(new InputStreamReader(p.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			result+=s+"\n";
			//System.out.println(s);
		}
		long t2=System.currentTimeMillis();
		tle=false;
		exeTime = (t2-t1)/(double)1000;
		//System.out.println("Executed in "+exeTime);
	}
	public void runCPP()throws Exception{
		long t1=System.currentTimeMillis();
		p=rt.exec(programName);
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
		//bw.write(2);
		//System.out.println(input);
		bw.write(input+"\n");
		bw.flush();
		//System.out.println("working");
		p.waitFor();
		
		
		//bw.write(2);
		BufferedReader br;
		if(p.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(p.getErrorStream()));
			error = true;
			
		}
		else{
			br=new BufferedReader(new InputStreamReader(p.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			result+=s+"\n";
			//System.out.println(s);
		}
		long t2=System.currentTimeMillis();
		tle=false;
		exeTime = (t2-t1)/(double)1000;
		//System.out.println("Executed in "+exeTime);
	}
	public void runPython2()throws Exception{
		long t1=System.currentTimeMillis();
		p=rt.exec("python2 "+programName);
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
		//bw.write(2);
		//System.out.println(input);
		bw.write(input+"\n");
		bw.flush();
		//System.out.println("working");
		p.waitFor();
		
		
		//bw.write(2);
		BufferedReader br;
		if(p.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(p.getErrorStream()));
			error = true;
			
		}
		else{
			br=new BufferedReader(new InputStreamReader(p.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			result+=s+"\n";
			//System.out.println(s);
		}
		long t2=System.currentTimeMillis();
		tle=false;
		exeTime = (t2-t1)/(double)1000;
		//System.out.println("Executed in "+exeTime);
	}
	public void runPython3()throws Exception{
		long t1=System.currentTimeMillis();
		p=rt.exec("python3 "+programName);
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
		//bw.write(2);
		//System.out.println(input);
		bw.write(input+"\n");
		bw.flush();
		//System.out.println("working");
		p.waitFor();
		
		
		//bw.write(2);
		BufferedReader br;
		if(p.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(p.getErrorStream()));
			error = true;
			
		}
		else{
			br=new BufferedReader(new InputStreamReader(p.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			result+=s+"\n";
			//System.out.println(s);
		}
		long t2=System.currentTimeMillis();
		tle=false;
		exeTime = (t2-t1)/(double)1000;
		//System.out.println("Executed in "+exeTime);
	}
	
}
