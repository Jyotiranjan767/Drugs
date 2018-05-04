package com.jyoti.theOnlineDrugstore.pagefactory;

import java.util.List;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class GiftCertificates {

	@FindBy(xpath=".//*[@id='Header']/div/div[1]/div/div[3]/div[1]/ul/li[4]/a")
	private WebElement giftCerificateLink;
	public WebElement giftCerificateLink(){
		return giftCerificateLink ;
	}
	@FindBy(xpath=".//*[@id='to_name']")
	private WebElement recipientName;
	public WebElement recipientName(){
		return recipientName ;
	}
	@FindBy(xpath=".//*[@id='to_email']")
	private WebElement  recipientEmail;
	public WebElement  recipientEmail(){
		return  recipientEmail ;
	}
	@FindBy(xpath=".//*[@id='message']")
	private WebElement yourMessage;
	public WebElement yourMessage(){
		return yourMessage ;
	}
	@FindBy(xpath=".//*[@id='certificate_amount']")
	private WebElement amount;
	public WebElement amount(){
		return amount ;
	}
	
	@FindBy(xpath=".//*[@id='agree2']")
	private WebElement iUnderstandCheck;
	public WebElement iUnderstandCheck(){
		return iUnderstandCheck ;
	}
	@FindBy(xpath=".//*[@class='FloatLeft']")
	private List<WebElement> giftForWhom;
	public List<WebElement> giftForWhom(){
		return giftForWhom ;
	}
	@FindBy(xpath=".//*[@id='frmGiftCertificate']/div/dl/dd[12]/input[1]")
	private WebElement preview;
	public WebElement preview(){
		return preview ;
	}
	@FindBy(xpath=".//*[@id='SaveCertificate']")
	private WebElement addGiftCertificateTCart;
	public WebElement addGiftCertificateTCart(){
		return addGiftCertificateTCart ;
	}
	
}
