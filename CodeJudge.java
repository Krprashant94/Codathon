import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.ObjectInputStream.GetField;

public class CodeJudge {
	public static void main(String[]args)throws Exception{
		System.out.println("OK");
		String pathname = args[0];
		String filename = args[1];
		String ext = args[2];
		String testCaseInputPath = args[3];
		String testCaseOutputPath = args[4];
		File testCaseOutputFile = new File(testCaseOutputPath);
		File testCaseInputFie = new File(testCaseInputPath);
		BufferedReader testCaseOutputReader = new BufferedReader(new FileReader(testCaseOutputFile));
		BufferedReader testCaseInpuReader = new BufferedReader(new FileReader(testCaseInputFie));
		String testCaseOuput = "";
		String testCaseInput = "";
		String finalMssg = "";
		int finalStatus = 0;
		double finalExeTime = 0.0;
		boolean error =false;
		int ch = '\0';
		while((ch=testCaseOutputReader.read())!=-1){
			testCaseOuput+=(char)ch;
		}
		ch='\0';
		while((ch=testCaseInpuReader.read())!=-1){
			testCaseInput+=(char)ch;
		}
		
		//System.out.println(testCase);
		CompileCode cc = new CompileCode();
		if(ext.equals("java") || ext.equals("c") || ext.equals("cpp")){
			error = cc.compileCode(pathname, filename, ext);
		}
		if(!error){
			CodeExecutor ce=null;
			if(ext.equals("java")){
				 ce=new CodeExecutor(pathname+" "+filename.substring(0,filename.indexOf(".")),ext,testCaseInput);//Total (programPath and name) ,extension,input
			}
			else if(ext.equals("c")){
				ce = new CodeExecutor(pathname+"/"+filename.substring(0,filename.indexOf(".")), ext,testCaseInput);
			}
			else if(ext.equals("cpp")){
				ce = new CodeExecutor(pathname+"/"+filename.substring(0,filename.indexOf(".")), ext,testCaseInput);
			}
			else if(ext.equals("py2")){
				ce = new CodeExecutor(pathname+"/"+filename, ext,testCaseInput);
			}
			else if(ext.equals("py3")){
				ce = new CodeExecutor(pathname+"/"+filename, ext,testCaseInput);
			}
			
			ce.setDaemon(true);
			ce.start();
			Thread.sleep(2000);
			if(ce.error){
				//System.out.println("Runtime error:- "+ce.result);
				finalMssg = ce.result;
				
			}
			else if(ce.tle){
				//System.out.println("Time Limit Exceeded!");
				finalStatus = 4;
			}
			else if(ce.result.equals(testCaseOuput)){
				finalStatus = 2;
				finalExeTime = ce.exeTime;
				//System.out.println("Correct Answer.");
			}
			else {
				finalStatus = 1;
				finalExeTime = ce.exeTime;
				//System.out.println("Wrong Answer.");
			}
		}
		else{
			//for compilation error:-
			//System.out.println("Compilation error");
			finalStatus = 0;
			finalMssg = cc.resultString;
		}
		System.out.println("{\"status\" : \""+finalStatus+"\", \"mssg\" : \""+finalMssg.replace("\"","&quot;").replace("\'","&quot;").replace("\n","<br/>")+"\", \"time\" : \""+finalExeTime+"\"}");
		
	}

}
