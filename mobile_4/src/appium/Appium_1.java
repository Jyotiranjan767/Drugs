package appium;

import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.BrowserType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;
import io.selendroid.client.SelendroidDriver;
import io.selendroid.common.SelendroidCapabilities;
import io.selendroid.standalone.SelendroidLauncher;

public class Appium_1 {

	WebDriver driver=null; 
	private SelendroidLauncher selendroidServer = null;
	@Test
	public void kdsf(){
		
		System.out.println("nfa");
		
	}
	@BeforeTest
	public void sda() throws MalformedURLException{
		DesiredCapabilities caps=SelendroidCapabilities.android();
		caps.setCapability(MobileCapabilityType.BROWSER_NAME, BrowserType.CHROME);
		caps.setCapability(MobileCapabilityType.PLATFORM, Platform.ANDROID);
		

		URL url=new URL("http://127.0.0.1:4723/wd/hub");
		//driver=new SelendroidDriver(caps);
	}
}
