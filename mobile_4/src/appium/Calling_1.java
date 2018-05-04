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

public class Calling_1 {

	WebDriver driver=null;
	@Test
	public void callMe() {
	
		driver.get("http.facebook.com");
	}
	@BeforeTest
	public void config() throws MalformedURLException {
		
		DesiredCapabilities caps=new DesiredCapabilities();
		caps.setCapability(MobileCapabilityType.BROWSER_NAME, BrowserType.CHROME);
		caps.setCapability(MobileCapabilityType.PLATFORM, Platform.ANDROID);
		caps.setCapability(MobileCapabilityType.PLATFORM_NAME, "Android");
		caps.setCapability(MobileCapabilityType.DEVICE_NAME, "LGE4455");
		caps.setCapability(MobileCapabilityType.VERSION, "4.1.2");
		
		URL url=new URL("http://127.0.0.1:4723/wd/hub");
		driver=(WebDriver) new SelendroidDriver(caps);
	}
}
