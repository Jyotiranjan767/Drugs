package com.jyoti.theOnlineDrugstore.ExcelLib;

import java.awt.AWTException;
import java.awt.Robot;
import java.util.Iterator;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.Alert;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;


public class CommonClasses {

	Select sel=null;
	WebDriverWait wait=null;
	Alert alert=null;
	Actions act=null;
	
	public void  waitForPageToLoad(int seconds,WebElement xpath ){
		wait=new WebDriverWait(Driver.driver,seconds);
		wait.until(ExpectedConditions.elementToBeSelected(xpath));
	}
	public void impli(int seconds){
		Driver.driver.manage().timeouts().implicitlyWait(seconds, TimeUnit.SECONDS);
	}
	public void selectByVisibleText(WebElement we,String eir){
		
		sel=new Select(we);
		sel.selectByVisibleText(eir);
		
	}
	  
    public void selectByIndex(WebElement we,int eir){
		
		sel=new Select(we);
		sel.selectByIndex(eir);
		
	}
 
    public Alert sendKeysAlert(){
    	alert=Driver.driver.switchTo().alert();
    	return alert;
    }
    public void accept(){ 
    	alert=Driver.driver.switchTo().alert();
    	alert.accept();
    }
    
    public void moveToElement(WebElement ele){
    	
    	act=new Actions(Driver.driver);
    	act.moveToElement(ele).build().perform();
    }
    
    public void getMeWindowsToHandle(){
    	
    	Set<String> windows=Driver.driver.getWindowHandles();
    	
    	Iterator<String> itr=windows.iterator();
    	while(itr.hasNext()){
    		itr.next();
    		String child=itr.next();
    		
    		Driver.driver.switchTo().window(child);
    	}
    }
    public Robot robo() throws AWTException{
		return new Robot();
	}

}
