package net.radzebra.itTalent ;
import net.radzebra.itTalent.dao.* ;

import java.util.*;
import java.io.*;
import java.lang.reflect.*;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
/**
* A simple Talent database to record group members' story.
* It based on sqlite and iBatis
*  taosheng.chen[at]gmail.com
*/
public class TalentManager{
    private String RESOURCE = "mybatisConfig.xml"; 
    private SqlSession SQL_SESSION ;
    private HashMap<Class, Object> MAPPERS_MAP = new HashMap<Class, Object>(7);
    /** An empty Talent instance*/
    public TalentManager()throws Exception{
        Reader reader = Resources.getResourceAsReader(RESOURCE); 
        this.SQL_SESSION = new SqlSessionFactoryBuilder().build(reader).openSession();

        this.SQL_SESSION.getConnection().setAutoCommit(true);
        this.MAPPERS_MAP.put(Talent.class, this.SQL_SESSION.getMapper(TalentMapper.class));

/*
        this.MAPPERS_MAP.put("confidentLevel",this.SQL_SESSION.getMapper(ConfidentLevelMapper.class);
        this.MAPPERS_MAP.put("contact",this.SQL_SESSION.getMapper(ContactMapper.class);
        this.MAPPERS_MAP.put("endorsement",this.SQL_SESSION.getMapper(EndorsementMapper.class);
        this.MAPPERS_MAP.put("tag",this.SQL_SESSION.getMapper(TagMapper.class);
        this.MAPPERS_MAP.put("talentStory",this.SQL_SESSION.getMapper(TalentStoryMapper.class);
        this.MAPPERS_MAP.put("talentTag",this.SQL_SESSION.getMapper(TalentTagMapper.class);
        this.MAPPERS_MAP.put("type",this.SQL_SESSION.getMapper(TypeMapper.class);
*/
    }
    /** A given id to manage a talent */
    public TalentManager(String id){
    }
    /** Add new talent in datbase*/
    public void addTalent(Talent talent)throws Exception{
       
        TalentMapper talentMapper = this.SQL_SESSION.getMapper(TalentMapper.class);
        talentMapper.insert(talent);
    } 
    /** simple add Object in to database*/
    public int addObject(Object obj)throws Exception{
        String mapperInsertName = obj.getClass().getName()+"Mapper.insert";
        return this.SQL_SESSION.insert(mapperInsertName,obj);
    }
    /** simple add Object in to database, the same as addObject() */
    public int insertObject(Object obj)throws Exception{
        return addObject(obj);
    }
    /** simple select Object by primarykey */
    public Object selectObject(String className,Object key)throws Exception{
        String mapperSelectName = className+"Mapper.selectByPrimaryKey";
        return this.SQL_SESSION.selectOne(mapperSelectName,key);
    }

    public void updateObject(Object obj)
	throws Exception{
        String mapperUpdateName = obj.getClass().getName()+"Mapper.updateByPrimaryKeySelective";
//        String mapperUpdateName = "net.radzebra.itTalent.dao."+objName+"Mapper.deleteByPrimaryKey";
        this.SQL_SESSION.update(mapperUpdateName,obj);
    }

    public void deleteByPrimaryKey(String objName, String primaryKey)
	throws Exception{
        String mapperDeleteName = "net.radzebra.itTalent.dao."+objName+"Mapper.deleteByPrimaryKey";
        this.SQL_SESSION.delete(mapperDeleteName,primaryKey);
    }

    public void deleteTalentById(String id){
        TalentMapper talentMapper = this.SQL_SESSION.getMapper(TalentMapper.class);
        talentMapper.deleteByPrimaryKey(id);
    }

    public List<Talent> selectTalentByTagDesc(String desc){
        TalentExample talentExample = new TalentExample();
        TalentMapper talentMapper = this.SQL_SESSION.getMapper(TalentMapper.class);
        List<Talent> talentList = talentMapper.selectByTagDesc(desc);
        return talentList ;
    }
    public List<Talent> selectTalentByEmail(String email){

        TalentExample talentExample = new TalentExample();
        TalentExample.Criteria criteria = talentExample.createCriteria();
        criteria.andEmailLike(email);
        TalentMapper talentMapper = this.SQL_SESSION.getMapper(TalentMapper.class);
        List<Talent> talentList = talentMapper.selectByExample(talentExample);
        return talentList ;
     
    }

    public static void main(String arg[])throws Exception{
        println("demo the Talent class");
        TalentManager tm = new TalentManager();

        println("create tm ");
        Talent t = new Talent();
	println("talent newed...");
        t.setName("radZebra-10");
        t.setCellPhone("02-3939889");
        t.setEmail("toBeDel3@gmail.com") ;
        t.setBirthYear("2011");
        t.setDesc("a default user of talent manager");

//        tm.addObject(t);
        t = (Talent)tm.selectObject( Talent.class.getName() ,"11");
        println(t.getName() );
        t.setBirthDate("2011-11-11");
        t.setName("updated!");
        tm.updateObject(t) ;

/*
	println("talent added...");
        List<Talent> listTalent = tm.selectTalentByEmail("%toBeDel%");
	println("select talent...by email:toBeDel");
        for (Talent oneTalent : listTalent) {
            println("talent:"+oneTalent);
            println("delete this talent...");
            tm.deleteTalentById(oneTalent.getId() );
   
        }
        println("select talent by tag.desc=java");
        listTalent = tm.selectTalentByTagDesc("java");
        for (Talent oneTalent : listTalent) {
            println("talent:"+oneTalent);
        }
  */     

    }



    // wrapper of System.out.println
    private static void println(Object msg){
        System.out.println(msg);
    }
}
