package com.jyoti.theOnlineDrugstore.pagefactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Paypal {

	@FindBy(id="email")
	private WebElement emailName;
	
	public WebElement email(){
		return emailName;
	}
	@FindBy(xpath=".//*[@id='password']")
    private WebElement password;
	
	public WebElement password(){
		return password;
	}
}
