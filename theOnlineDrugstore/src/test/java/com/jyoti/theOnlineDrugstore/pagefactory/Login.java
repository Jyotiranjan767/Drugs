package com.jyoti.theOnlineDrugstore.pagefactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Login {

	@FindBy(xpath=".//*[@id='Header']/div/div[1]/div/div[3]/div[1]/ul/li[2]/div/a[1]")
	private WebElement signIn;
	
	@FindBy(xpath=".//*[@id='login_email']")
	private WebElement userName;
	
	@FindBy(xpath=".//*[@id='login_pass']")
	private WebElement password;
	
	@FindBy(xpath=".//*[@id='LoginButton']")
	private WebElement submit;
	
	public WebElement signIn(){
		
		return signIn;
	}
	
   public WebElement userName(){
		
		return userName;
	}

    public WebElement password(){
	
	return password;
}
    public WebElement submit(){
    	return submit;
    }
}
