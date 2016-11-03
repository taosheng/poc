package net.radzebra.itTalent.servlet ;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.*;
import net.radzebra.itTalent.*;
import net.radzebra.itTalent.dao.*;
import com.google.gson.*;
import com.google.gson.reflect.*; 

public class TalentServlet extends HttpServlet{

    private void addObject(String className, BufferedReader requestContent)
	throws IOException,Exception{
            Gson gson = new Gson();
            Map<String, Class> classMap = new HashMap<String, Class>(7); 
            classMap.put("Talent",Talent.class);
	    Object obj = gson.fromJson(requestContent, classMap.get("Talent"));
	    TalentManager tManager = new TalentManager();
            tManager.addObject(obj);
    }
    private void updateObject(String className, BufferedReader requestContent)
	throws IOException,Exception{
            Gson gson = new Gson();
            Map<String, Class> classMap = new HashMap<String, Class>(7); 
            classMap.put("Talent",Talent.class);
	    Object obj = gson.fromJson(requestContent, classMap.get("Talent"));
	    TalentManager tManager = new TalentManager();
            tManager.updateObject(obj);
    }
    private void deleteObject(String className, BufferedReader requestContent)
	throws IOException,Exception{
            Gson gson = new Gson();
	    Map<String, String> toDelMap = 
		gson.fromJson(requestContent, new TypeToken<Map<String, String>>() {}.getType() );
	    TalentManager tManager = new TalentManager();
            tManager.deleteByPrimaryKey(className, toDelMap.get("primarykey"));
    }
    private String selectObject(String className, BufferedReader requestContent)
	throws IOException,Exception{
            String result ="";
            if(className.equals("talent.byEmail")){
                result = result + "[";
                Gson gson = new Gson();
	        Map<String, String> toSelectMap = 
		    gson.fromJson(requestContent, new TypeToken<Map<String, String>>() {}.getType() );
	        TalentManager tManager = new TalentManager();
                List<Talent> talentList = tManager.selectTalentByEmail(toSelectMap.get("email"));
                for (Talent t : talentList){ 
                    result = result +  gson.toJson(t) +",";
                } 
                result = result + "]";
            }else if(className.equals("talent.byPrimarykey")){
                Gson gson = new Gson();
	        Map<String, String> toSelectMap = 
		    gson.fromJson(requestContent, new TypeToken<Map<String, String>>() {}.getType() );
	        TalentManager tManager = new TalentManager();
                Talent t = (Talent) tManager.selectObject(Talent.class.getName(),toSelectMap.get("primarykey"));
                result = result +  gson.toJson(t) ;

	    }else{
                throw new Exception("have not support: "+ className+" yet!" );
            }
            return result;
    }

    public void doGet(HttpServletRequest req, HttpServletResponse res)
        throws ServletException,IOException{
	res.setContentType("text/plain; charset=UTF-8");
        res.setCharacterEncoding("UTF-8");
        PrintWriter output = res.getWriter();
        StringBuffer outputBuffer = new StringBuffer();
//	ServletContext context = req.getContext();
        String contextPath = req.getContextPath();
        String requestURI = req.getRequestURI();
	BufferedReader  reader = req.getReader();
        // TODO a config to determind the actions
        String[] requestURIParts = requestURI.split("/");
        String api = requestURIParts[2];

        if(!api.equals("api")){ return ; }

        String targetClass = requestURIParts[3];
        String targetAction = requestURIParts[4] ;
        try{

            if( targetAction.equals("add") || targetAction.equals("insert")) {
                addObject(targetClass,reader);
            }else if(targetAction.equals("delete")){
                deleteObject(targetClass,reader) ;
            }else if(targetAction.equals("update")){
                updateObject(targetClass,reader) ;
            }else if(targetAction.equals("select")){
                String result = selectObject(targetClass,reader) ;
                outputBuffer.append(result) ;
            }else{
                outputBuffer.append("{'response':'no support such action:"+targetAction+"'}");
            }
      //      List<Talent> listTalent = tm.selectTalentByEmail("%rad%");
      //      for (Talent oneTalent : listTalent) {
      //          outputBuffer.append("talent:"+oneTalent+" ");
      //      }
        }catch(Exception e){
            //throw new ServletException(e);
            outputBuffer.append("{'exception':'"+e+"'}");
	}
        
	output.println(outputBuffer.toString() );
        output.close();
    }

    public void doPost(HttpServletRequest req, HttpServletResponse res)
        throws ServletException, IOException{
        this.doGet(req,res);
    }
}

