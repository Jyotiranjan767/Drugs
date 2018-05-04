package appium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import io.selendroid.standalone.SelendroidConfiguration;
import io.selendroid.standalone.SelendroidLauncher;

public class Selendroid_1 {

	private SelendroidLauncher selendroidServer=null;
	private WebDriver driver=null;
	
	@Test
	public void shouldSearchWithEbay(){
		driver.get("www.m.ebay.de");
		
	}@BeforeTest
	public void conifug() throws Exception{
		if(selendroidServer!=null){
			selendroidServer.stopSelendroid();
		}
		SelendroidConfiguration config=new SelendroidConfiguration();
		selendroidServer=new SelendroidLauncher(config);
		
		DesiredCapabilities caps =new  SelendroidCapabilities();//.android();

	   /// driver = (WebDriver) new SelendroidDriver(caps);
		driver=new FirefoxDriver();
	}
	@AfterTest
	public void stopServer(){
		if(driver!=null)
			driver.quit();
		if(selendroidServer!=null)
			selendroidServer.stopSelendroid();
		
	}
}
