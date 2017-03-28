package com.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class NaukriLogin {

	@FindBy(xpath=".//*[@id='emailTxt']")
	private WebElement userName;
	public WebElement userName(){
		return userName;
	}
	@FindBy(xpath=".//*[@id='pwd1']")
	private WebElement password;
	public WebElement password(){
		return password;
	}
	@FindBy(xpath=".//input[@id='sbtLog']")
	private WebElement submit;
	public WebElement submit(){
		return submit;
	}
}
