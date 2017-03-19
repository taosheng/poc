import net.radzebra.itTalent.dao.*;
import net.radzebra.itTalent.*;
import com.google.gson.*;
import com.google.gson.reflect.*;
public class TryGson{

	public static void main(String[] arg)throws Exception{
		println("try GSON");
  		Gson gson = new Gson();
		String talentJson="{'name':'testname','firstname':'Dan','lastname':'Daley','email':'some2@gmail.com'}";
		String storyJson="{'name':'testname','firstname':'Dan','lastname':'Daley','email':'some2@gmail.com'}";
		Talent t = gson.fromJson(talentJson,Talent.class);
		println(t);
		println("name: "+ t.getName());
		println("id: "+t.getId());
		println("email: "+t.getEmail());
                TalentManager tm = new TalentManager();
                println(tm.addObject(t));
                println(t.getId());
		
	}

	public static void println(Object msg){
		System.out.println(msg);
	}
}
