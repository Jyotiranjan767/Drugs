package com.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class ViewProfile {

	@FindBy(xpath="//*[@id='colL']/div[2]/div[1]/a[1]")
	private WebElement viewProfileLink;
	public WebElement viewProfileLink(){
		return viewProfileLink;
	}
	@FindBy(xpath=".//*[@id='uploadLink']")
	private WebElement uploadResumeLink;
	public WebElement uploadResumeLink(){
		return uploadResumeLink;
	}
	@FindBy(xpath=".//*[@id='attachCV']")
	private WebElement browse;
	public WebElement browse(){
		return browse;
	}
	@FindBy(xpath=".//*[@id='editForm']/div[7]/button")
	private WebElement save;
	public WebElement save(){
		return save;
	}
	
}
