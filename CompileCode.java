import java.io.BufferedReader;
import java.io.InputStreamReader;


class CompileCode{
	public boolean error=false;
	public String resultString = "";
	public  boolean compileCode(String pathname,String filename,String ext){
		
		try {
			if(ext.equalsIgnoreCase("java")){
				return compileJava(pathname, filename, ext);
				
			}
			else if(ext.equalsIgnoreCase("c")){
				return compileC(pathname, filename, ext);
			}
			else if(ext.equalsIgnoreCase("cpp")){
				return compileCPP(pathname, filename, ext);
			}
			else{
				return false;
			}
		} catch (Exception e) {
			error=true;
			
			System.out.println("Compilation terminated unexpectedly.");
			return error;
		}
	}
	public boolean  compileJava(String pathname,String filename,String ext)throws Exception{
		Runtime rt=Runtime.getRuntime();
		Process compile=rt.exec("javac "+pathname+"/"+filename);
		compile.waitFor();
		BufferedReader br;
		if(compile.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(compile.getErrorStream()));
			//error=true;
		}
		else{
			br=new BufferedReader(new InputStreamReader(compile.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			error=true;
			//System.out.println(s);
			resultString+=s+"\n";
		}
		return error;
	}
	public boolean compileC(String pathname,String filename,String ext)throws Exception{
		System.out.println("gcc "+pathname+"/"+filename+" -o "+filename.substring(0,filename.indexOf(".")));
		Runtime rt=Runtime.getRuntime();
		Process compile=rt.exec("gcc "+pathname+"/"+filename+" -o "+pathname+"/"+filename.substring(0,filename.indexOf("."))+"-lm");
		compile.waitFor();
		BufferedReader br;
		if(compile.exitValue()!=0){
			br=new BufferedReader(new InputStreamReader(compile.getErrorStream()));
			//error=true;
		}
		else{
			br=new BufferedReader(new InputStreamReader(compile.getInputStream()));
		}
		String s;
		while((s=br.readLine())!=null){
			error=true;
			System.out.println(s);
		}
		return error;
	}
	public boolean compileCPP(String pathname,String filename,String ext)throws Exception{
		//System.out.println("gcc "+pathname+"/"+filename+" -o "+filename.substring(0,filename.indexOf(".")));
				Runtime rt=Runtime.getRuntime();
				Process compile=rt.exec("g++ "+pathname+"/"+filename+" -o "+pathname+"/"+filename.substring(0,filename.indexOf(".")));
				compile.waitFor();
				BufferedReader br;
				if(compile.exitValue()!=0){
					br=new BufferedReader(new InputStreamReader(compile.getErrorStream()));
					//error=true;
				}
				else{
					br=new BufferedReader(new InputStreamReader(compile.getInputStream()));
				}
				String s;
				while((s=br.readLine())!=null){
					error=true;
					System.out.println(s);
				}
				return error;
	}
	}
