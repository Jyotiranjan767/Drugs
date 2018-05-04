package com.jyoti.theOnlineDrugstore.ExcelLib;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

public class Driver {
 
	
	private static  ChromeDriver driver1(){
		
		ChromeOptions co =new ChromeOptions();
		co.addArguments("--disable-notifications");
		
		System.setProperty("webdriver.chrome.driver","C:\\Users\\luckie\\Downloads/chromedriver.exe" );
	   return new ChromeDriver(co);
	}
	
	public static WebDriver driver=driver1();//new InternetExplorerDriver();
	
}
