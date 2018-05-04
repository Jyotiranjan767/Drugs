package com.jyoti.theOnlineDrugstore.BusinessClass;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import com.gargoylesoftware.htmlunit.Page;
import com.jyoti.theOnlineDrugstore.ExcelLib.CommonClasses;
import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;
import com.jyoti.theOnlineDrugstore.pagefactory.Checkout;
import com.jyoti.theOnlineDrugstore.pagefactory.GiftCertificates;
import com.jyoti.theOnlineDrugstore.pagefactory.Login;
import com.jyoti.theOnlineDrugstore.pagefactory.Nutrition;
import com.jyoti.theOnlineDrugstore.pagefactory.Paypal;
import com.thoughtworks.selenium.webdriven.commands.AlertOverride;
import com.thoughtworks.selenium.webdriven.commands.IsAlertPresent;

public class BusinessComponents {

	Login login=PageFactory.initElements(Driver.driver, Login.class);
	Nutrition nutri=PageFactory.initElements(Driver.driver, Nutrition.class);
	Checkout co=PageFactory.initElements(Driver.driver, Checkout.class);
	Paypal pp=PageFactory.initElements(Driver.driver, Paypal.class);
	GiftCertificates gc=PageFactory.initElements(Driver.driver, GiftCertificates.class);
	CommonClasses cc=new CommonClasses();
	public void logBusi() throws InterruptedException{
		
		Thread.sleep(3000);
		login.signIn().click();
		Thread.sleep(3000);
		login.userName().sendKeys("zapakjyoti@gmail.com");
		Thread.sleep(3000);
		login.password().sendKeys("jyoti@348");
		
		Thread.sleep(3000);
		login.submit().click();
		//IsAlertPresent su=new IsAlertPresent((AlertOverride) Driver.driver.switchTo().alert());
		/*if(su){
			
		}*/
	}
	
	public void nutriBags(){
		
		cc.moveToElement(nutri.nutriSelect());
		//nutri.nutriSelect();
		//cc.selectByVisibleText(nutri.nutriSelect(), "Vitamins & Supplements");
		cc.impli(3);
		nutri.vita().click();
		cc.impli(12);
	}
	
	public void addToCart(){
		System.out.println("Entering into add to cart,,,,,,,,,,,,,,****************(*");
		for(int i=0;i<nutri.welleseCalcium().size();i++){
			System.out.println(nutri.welleseCalcium().size()+"*&&&&&&&&&&&&&&&&********");
		List<WebElement> ds=nutri.welleseCalcium().get(i).findElements(By.tagName("div"));
		for(WebElement we:ds){
			System.out.println( we.getText()); 
			
		if(we.getText().contains("Add To Cart")){
			we.click();
		}else
			System.out.println("Match not found ");
		}
	}
		co.checkout().click();

		
		cc.getMeWindowsToHandle();
		pp.email().sendKeys("joryi@gmail.com");
		pp.password().sendKeys("srr3r232");
	}
	public void addGifts() throws InterruptedException{
		gc.giftCerificateLink().click();
		gc.recipientName().sendKeys("afnaf");
		gc.recipientEmail().sendKeys("jyotiranjan8787@gmail.com");
		gc.yourMessage().sendKeys("Im thankfully resoloved my message to make you feel better");
		gc.amount().sendKeys("25");
		Thread.sleep(2333);
    	/*if(!gc.iUnderstandCheck().isSelected()){
			System.out.println("FJSKS)))))))))))))(((sssssssssss Iusnd");
			gc.iUnderstandCheck().click();
		}*/
	
		List<WebElement> dsf= gc.giftForWhom();
		for(int i=0;i<dsf.size();i++){
			Thread.sleep(2333);
			System.out.println("&RGYYYYYYYYY size "+ dsf.size());
		if(dsf.get(i).findElements(By.tagName("div")).get(i).getText().equalsIgnoreCase("boy")){
			System.out.println("*****************##########");
			Thread.sleep(2333);
			dsf.get(i).findElements(By.tagName("div")).get(i).click();
		}else{
			System.out.println(dsf.get(i).findElements(By.tagName("div")).get(i).getText());
			
		}
		Thread.sleep(2333);
	}
		gc.addGiftCertificateTCart().click();
	}
	

	
}

