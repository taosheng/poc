
package net.smalldata ;
import java.io.*;
import java.util.*;

public class SimpleTemplateMerger{
    private String TEMPLATE_PROPERTIES_FILE = "template.properties";
    private String TEMPLATE_FOLDER = "template";
    private String OUTPUT_FOLDER = "output";
    public SimpleTemplateMerger(String templateFolder, String propertiesFile){
   	if(templateFolder != null){
            this.TEMPLATE_FOLDER = templateFolder ;
        }
        if(propertiesFile != null){
            this.TEMPLATE_PROPERTIES_FILE = propertiesFile ;
        }
    }
    
    public void merge()throws Exception{

        FileReader propertiesReader = new FileReader(this.TEMPLATE_PROPERTIES_FILE);
        Properties prorerties = new Properties();
        prorerties.load(propertiesReader);
        Set propertiesKeySet =   prorerties.keySet() ;
        File templateFolderPath = new File(this.TEMPLATE_FOLDER) ;
        File[] templateFiles = templateFolderPath.listFiles() ;

        for(int i = 0 ; i < templateFiles.length ; i++){
            if(!templateFiles[i].getName().endsWith(".temp")){
                continue ;
            }
            println("handle file: " + templateFiles[i].getName());
            String outputfileName = templateFiles[i].getPath().replace(".temp","");
            println("output file: " + outputfileName);
            BufferedReader in = new BufferedReader(new FileReader(templateFiles[i]));
            PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outputfileName)));

            String line = in.readLine() ;
            while(line != null ){
	        Iterator keysIterator = propertiesKeySet.iterator();
                while(keysIterator.hasNext() ){
                    String keyName =  (String)keysIterator.next() ;
                    String tofindkey = "${"+ keyName +"}" ;
                    String replaceString = prorerties.getProperty(keyName).trim()  ;
                    if(!line.contains(tofindkey)){
                        continue ; 
                    }

                    if(replaceString.contains(",")){
                        String[] parts = replaceString.split(",") ;
                        String tmp = "";
                        for(int p=0; p< parts.length ;p++){
                            tmp = tmp + line.replace(tofindkey, parts[p])+"\n";
                        }
                        line = tmp;
                    }else{
                        line = line.replace(tofindkey,replaceString );
                    }
                }

                out.write(line+"\n");
                line = in.readLine();

            }
            out.flush();
        }

        // get template file from template folder
    }


    private static void println(Object msg)throws Exception{
        System.out.println(msg); 
    }
}
