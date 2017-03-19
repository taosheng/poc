package net.radzebra.itTalent.json ;

import net.radzebra.itTalent.dao.*;
import com.google.gson.*;
import com.google.gson.reflect.*;
import java.util.*;

public class Transformer{
/**
*   Transfer json string to myBatis's bean instance.
*/
    Gson GSON = null;
    Map<String, Class> DAO_NAME_CLASS_MAP= null;

    public Transformer(){
        this.GSON = new Gson();
        this.DAO_NAME_CLASS_MAP = new HashMap<String, Class>(7);
  
        this.DAO_NAME_CLASS_MAP.put("talent",Talent.class);
        this.DAO_NAME_CLASS_MAP.put("contact",Contact.class);
    }

    public Object getObjectFromJson(String className, String jsonString)
	throws Exception{

        Object obj = this.GSON.fromJson(jsonString, this.DAO_NAME_CLASS_MAP.get(className) )  ;
        return obj;
    }
    public String getJsonFromObject(Object obj)
	throws Exception{

        return this.GSON.toJson(obj) ;
    }

    public static void main(String[] args)throws Exception{
        println("Transformer: transfer between json and myBatis dao object");

        Transformer tf = new Transformer();
        Talent t = (Talent)tf.getObjectFromJson("talent","{'name':'tss','email':'xxx@gmail'}");

	println(t.getName());
        println(tf.getJsonFromObject(t));
        
    }
   
    private static void println(Object msg){
        System.out.println(msg);
    }
}
