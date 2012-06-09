package com.vul3fm0fm0 ;
import org.apache.http.client.HttpClient ;
import org.apache.http.*;
import org.apache.http.impl.client.DefaultHttpClient ;
import org.apache.http.client.methods.*; 
import javax.xml.parsers.*;
import java.io.* ;
import org.w3c.dom.*;

 
public class test{

    public static void main(String[] args)throws Exception{
        println("musicbrainz test") ;
        HttpClient mzclient = new DefaultHttpClient();

       // Prepare a request object
        String qstring="http://musicbrainz.org/ws/2/release?artist=3033ce2b-2fb2-408e-8c5a-aea48592d7bc&limit=50" ;
        HttpGet httpget = new HttpGet(qstring);
        HttpResponse response = mzclient.execute(httpget);

        println(response.getStatusLine());

        HttpEntity entity = response.getEntity();
 
        if (entity != null) {
             println("prepare entity") ;
             InputStream instream = entity.getContent();

//             BufferedReader reader = new BufferedReader(
//               new InputStreamReader(instream));

         DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();


            Document document = builder.parse(instream) ; 
            println(document.getDocumentElement().getTagName() ) ;


  
	/*
             String line  = "" ;
             line = reader.readLine();
            
             while(line != null ){
                 println(line);
                 line = reader.readLine();
             }
         */


        }
        
    }

    public static void println(Object msg){
        System.out.println(msg);
    }
}
