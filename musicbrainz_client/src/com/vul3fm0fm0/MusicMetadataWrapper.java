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
        println("musicbrainz test:") ;
        String artistName = "Jolin" ;
        if( args[0] != null && args[0].length() != 0 ){
		artistName = args[0] ;
	} 
        println("try to find artist name:" + artistName ) ;

	MusicMetadataWrapper mmw = new MusicMetadataWrapper();
	String artistId = mmw.findArtist(artistName);
        println("artist id = "+ artistId );

        String findReleaseUrl = "http://musicbrainz.org/ws/2/release?artist="+artistId+"&limit=50" ;
        println("find release query url="+findReleaseUrl ); 

        Document releaseDoc = mmw.getQueryResultDocument(findReleaseUrl);
        println("show all the release title"); 
        NodeList titleNodeList = releaseDoc.getDocumentElement().getElementsByTagName("title");

        for(int i = 0; i< titleNodeList.getLength() ;i++){
		println(titleNodeList.item(i).getFirstChild().getNodeValue());
	}


        
    }

    public static void println(Object msg){
	try{
        PrintStream out = new PrintStream(System.out, true, "UTF-8");
        out.println(msg);
	}catch(Exception e){
		System.out.println("damn!"+e);
	}
    }
}
