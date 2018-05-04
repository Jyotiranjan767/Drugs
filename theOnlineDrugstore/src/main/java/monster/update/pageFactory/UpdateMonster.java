package monster.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UpdateMonster {

	@FindBy(xpath=".//*[@id='update_pfbtn']/a")
	private WebElement updateProfile;
	public WebElement updateProfile(){
		return updateProfile;
	}
	
	@FindBy(xpath=".//*[@id='res0']/div/div[2]/div/a[2]")
	private WebElement editResume;
	public WebElement editResume(){
		return editResume;
	}
	@FindBy(xpath=".//*[@id='wordresume']")
	private WebElement chooseFile;
	public WebElement chooseFile(){
		return chooseFile;
	}
	@FindBy(xpath=".//*[@id='ResumeUploadForm']/div[9]/input")
	private WebElement submitButton;
	public WebElement submitButton(){
		return submitButton;
	}

}
