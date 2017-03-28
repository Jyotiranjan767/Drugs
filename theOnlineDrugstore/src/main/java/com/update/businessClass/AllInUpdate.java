package com.update.businessClass;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.openqa.selenium.support.PageFactory;

import com.jyoti.theOnlineDrugstore.ExcelLib.CommonClasses;
import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;
import com.update.pageFactory.LogoutNaukri;
import com.update.pageFactory.NaukriLogin;
import com.update.pageFactory.ViewProfile;

public class AllInUpdate {

	NaukriLogin nl=PageFactory.initElements(Driver.driver,NaukriLogin.class);
	ViewProfile vp=PageFactory.initElements(Driver.driver,ViewProfile.class);
	LogoutNaukri ln=PageFactory.initElements(Driver.driver,LogoutNaukri.class);
	
	CommonClasses cc=new CommonClasses();
	public void login() throws AWTException{
		
		Driver.driver.get("https://login.naukri.com/nLogin/Login.php");
		nl.userName().sendKeys("jyotiranjan976@gmail.com");
		nl.password().sendKeys("hritik");
		cc.impli(3);
		cc.robo().keyPress(KeyEvent.VK_ENTER);
		cc.robo().keyRelease(KeyEvent.VK_ENTER);
		//nl.submit().click();
		System.out.println("eqehiq ruqir****************");
		}
	public void resumeUpload(String ri) throws AWTException, InterruptedException {
		
		vp.viewProfileLink().click();
		vp.uploadResumeLink().click();
		cc.impli(3);
		vp.browse().click();
		cc.impli(13);
		Thread.sleep(1000);
		/*for(int i=0;i<ri.length();i++){
			cc.impli(3);
			char c=ri.charAt(i);
		System.out.println(i+"**********************");
		  // cc.robo().keyPress(c);
		  // cc.robo().keyRelease(c);
		}*/
	//	cc.sendKeysAlert().sendKeys("Automation2017.docx");;
		cc.robo().keyPress(KeyEvent.VK_A);
		cc.robo().keyRelease(KeyEvent.VK_A);
		cc.robo().keyPress(KeyEvent.VK_U);
		cc.robo().keyRelease(KeyEvent.VK_U);
		Thread.sleep(1000);
		cc.robo().keyPress(KeyEvent.VK_DOWN);
		cc.robo().keyRelease(KeyEvent.VK_DOWN);
		Thread.sleep(1000);
		cc.robo().keyPress(KeyEvent.VK_ENTER);
		cc.robo().keyRelease(KeyEvent.VK_ENTER);
		cc.robo().keyPress(KeyEvent.VK_ENTER);
		cc.robo().keyRelease(KeyEvent.VK_ENTER);
		vp.save().click();
	//	vp.browse().sendKeys("Automation2017.docx");
		
	} 
	public void logout() throws InterruptedException{
		cc.moveToElement(ln.myNaukri());
		Thread.sleep(1000);
	    ln.logout().click();
	//	Driver.driver.close();
	}
}
