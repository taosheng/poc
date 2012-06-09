package com.vul3fm0fm0 ;
import org.apache.http.client.HttpClient ;
import org.apache.http.*;
import org.apache.http.impl.client.DefaultHttpClient ;
import org.apache.http.client.methods.*; 
import javax.xml.parsers.*;
import java.io.* ;
import org.w3c.dom.*;

 
public class MusicMetadataWrapper{

    private String QUERY_URL="http://musicbrainz.org/ws/2/";

    private Document getQueryResultDocument(String queryString)throws Exception{

        HttpClient mzclient = new DefaultHttpClient();
        HttpGet httpget = new HttpGet(queryString);
        HttpResponse response = mzclient.execute(httpget);
        HttpEntity entity = response.getEntity();
 
        if (entity != null) {
             println("prepare entity") ;
             InputStream instream = entity.getContent();
         DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();

            Document document = builder.parse(instream) ; 
	    return document ;
        }else{
	    return null;
	}

//getElementsByTagName(String name) 

    }
  
    public String findArtist(String name)throws Exception{
	String id ="" ;
        String queryString = this.QUERY_URL + "artist?query="+name;
        Document artistDoc = getQueryResultDocument(queryString) ;

        NodeList nl = artistDoc.getDocumentElement().getElementsByTagName("artist")  ;
      
        id = nl.item(0).getAttributes().getNamedItem("id").getNodeValue() ;
	return id;
    }
    public static void main(String[] args)throws Exception{
        println("musicbrainz test") ;

	MusicMetadataWrapper mmw = new MusicMetadataWrapper();
	String artistId = mmw.findArtist("Jolin");
        println( artistId );

        
       // Prepare a request object
//        String qstring="http://musicbrainz.org/ws/2/release?artist=3033ce2b-2fb2-408e-8c5a-aea48592d7bc&limit=50" ;

        
    }

    public static void println(Object msg){
        System.out.println(msg);
    }
}
