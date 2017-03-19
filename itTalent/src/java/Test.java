import com.google.gson.*;
import com.google.gson.reflect.*;
import java.util.*;

public class Test{
	public static void main(String[] argv)throws Exception{
	/*	String myString = new JSONObject().put("JSON", "Hello, World!").toString();
		println(myString);
                String fromWeb ='{"JSON":"Hello, World!"}';
	*/
		Gson gson = new Gson();
		String requestMap="{\"name\":\"Tao\",\"email\":\"t@gmail.com\"}"; 
		Map<String, String> decoded = 
			gson.fromJson(requestMap, new TypeToken<Map<String, String>>() { }.getType() );
		println(decoded.get("name"));
	}

	private static void println(Object o)throws Exception{
		System.out.println(o);
	}
}
