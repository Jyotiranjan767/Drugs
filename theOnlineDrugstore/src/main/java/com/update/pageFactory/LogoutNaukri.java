package com.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LogoutNaukri {

	@FindBy(xpath=".//*[@id='mainHeader']/div/div/ul[2]/li[2]/a")
	private WebElement myNaukri;
	public WebElement myNaukri(){
		return myNaukri;
	}
	@FindBy(xpath="	.//*[@id='mainHeader']/div/div/ul[2]/li[2]/div/ul/li[5]/a")
	private WebElement logout;
	public WebElement logout(){
		return logout;
	}
}
