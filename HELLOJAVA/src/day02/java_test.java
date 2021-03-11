package day02;

import java.io.File;

public class java_test {
	String folder = "d:/contents";
	File contents = new File(folder);
	
	String[] children = contents.list();
	
//	for(String child : children){
//		System.out.println(child);
//	}
}
