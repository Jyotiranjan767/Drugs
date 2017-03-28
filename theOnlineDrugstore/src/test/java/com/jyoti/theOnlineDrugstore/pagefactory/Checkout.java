package com.jyoti.theOnlineDrugstore.pagefactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Checkout {

	@FindBy(xpath=".//*[@id='PayPalExpressCheckoutButton']")
	private WebElement checkout;
	
	public WebElement checkout(){
		return checkout;
	}
	
	
}
