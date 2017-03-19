package net.smalldata ;
import java.io.*;
import java.util.*;

public class Autogen{
    private static String templateProtertiesFile = "template.properties";
    private static String templateFolder = "template";
    public static void main(String[] argv)throws Exception{
        SimpleTemplateMerger stm = new SimpleTemplateMerger(templateFolder,templateProtertiesFile);

	stm.merge() ;
        // get template file from template folder
    }


    private static void println(Object msg)throws Exception{
        System.out.println(msg); 
    }
}
