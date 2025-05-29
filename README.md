Credit to [https://github.com/gsarti/paperpile-notion](https://github.com/mindemory/notion_paperpile/tree/main) as I modified the files they wrote. 

# Welcome to a Biologist's procrastination project to export Paperpile references into a Notion database!

These instructions are for Mac as that is what I have. Paperpile and Notion are both available on other platforms, so I'm sure there are ways to adapt this.  
These instructions are suitable for beginners because I am writing them for my past self, who had not yet spent hours fighting with ChatGPT and getting multiple headaches. Enjoy and if I've explained everything well, you hopefully don't get a headache.   
This file is not entirely finished - I will eventually write out the Notion Integration steps instead of linking you to it, because you don't need to follow that entire tutorial to get this to work. 

There are 3 big elements we are working with:
1. Notion page to which you want your papers exported, along with a Notion "Integration".
2. Github repository along with local files.
3. Paperpile Bibtex export, which connects to your Github.

## INSTRUCTIONS

#### First, we will start with Github.

Extra step for Windows:
Download Git as Terminal on Windows does not by default have git installed unlike Linux/Mac ````https://git-scm.com/downloads/win````. Run through the installation and make sure to select _“Git from the command line and also from 3rd-party software”_ when prompted (this is already the recommended option). Then you can open Terminal on Windows and run ````git --version```` to check it is intalled. 

1. Make a new repository.
2. Open terminal and clone this repo to yours (it should hopefully have all the tutorial data as I started by cloning the Notion tutorial repo).

> Go to the repository and press the green "Code" button at the top right.  
> Copy the URL.  
> Open Terminal (CMD+Space and search for Terminal).  
> Run ```git clone <repository-URL>```.

3. The ```origin``` remote will link to this github instead of yours so you need to change this.
> In terminal, use ```git remote set-url origin https://github.com/your-username/my-repo.git```.  
> You then need to add your files to your Github (which will be empty). To do this, run ```git add .``` - this tells Github 'This is the change I want to make'. You can do this for multiple files, which is why I think it's different from a _commit_.  
> Then you need to run a _commit_ ```git commit -m 'Initial commit'``` - this tells Github 'These are all the changes I will make this time'.  
> Then you _push_ ```git push -u origin main``` - which means you are saving your local files onto Github. Beware of the fact that if what's on Github is different from what you have locally, you will get a headache trying to sort it out.  

#### Let's move to Notion now.  

4. Follow Notion integration tutorial [here](https://developers.notion.com/docs/create-a-notion-integration) up until making the database in localhost - you will also get the integration secret from this process.
5. You must make a new Notion page with the template below. You must have the same columns with the same spelling and spacing or you'll need to modify the code. You're welcome to do this but I can't help you, since I don't know who you are and what changes you want. Ensure you keep this database empty for now. 

> The columns are Topic, Status, [Author, Year] (you must write it like this i.e. with the space and comma in between Author and Year not with the square brackets otherwise it will return an error), Journal, Key Takeaway, Summary, Title, Methods. Be careful with capitalisation and spaces as I think the code will take exception to any differences. 
> <img width="1257" alt="Screenshot 2025-05-23 at 13 47 21" src="https://github.com/user-attachments/assets/78e792c9-ec00-4d22-82f4-0b5a70a48531" />

6. Click on database/table and "Open as full page" - THIS is where you can find the correct database_id! If you don't do this, you will get the page id instead and spend ages trying to figure out why you're getting errors. Hopefully one of the many headaches I'll save you from.  

> This is your new page (here 'Project') with the 'database'/'table' associated with it. Click on the table and open as full page.
> <img width="374" alt="Screenshot 2025-05-23 at 13 42 43" src="https://github.com/user-attachments/assets/476c4a1d-93a9-453b-a665-39207caa38d2" />

> It will look like this - in the top right, click the 3 dots and select 'Copy link'.
> <img width="1278" alt="Screenshot 2025-05-23 at 13 41 28" src="https://github.com/user-attachments/assets/3bccee14-d1df-42e5-a2e8-1bdb2f4fea17" />

> You will get something like this "https://www.notion.so/Project-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?pvs=4" - the 32 characters replaced with x here is your database_id.

#### Return to your Terminal.

7. Create a new file "notion_ids.csv" in the directory ABOVE your project folder (this will be within folder /examples) - this needs to look like below. You should add this to your gitignore file as you should not be putting this data online! (Unless you want random references from strangers in your Notion table?)

> I suggest typing this out yourself and not copy-pasting it as I had to add spaces to create a line break in markdown (which is this readme file format) and so might return an error.

> database_id,NOTION_KEY  
> [your database_id]  
> [your integration secret - do NOT write secret_ in front of it, just copy/paste it from the notion page]  

### Before you do the next step, you should ```push``` your files to your Github repo. We want to do this before the next step, because the next step creates your references.bib file straight into Github. And if your local files don't match the Github and you want files from both places, you will get _another_ headache. I am trying to save you lots of headaches. 

#### Next, we need the final element, which is the Paperpile references. 
8. Go to Paperpile. In the top right corner where your user photo is, you will see "Worflows and Integrations".  
<img width="322" alt="Screenshot 2025-05-23 at 15 39 11" src="https://github.com/user-attachments/assets/7e3e61bd-740d-4da5-99b1-2ee5cfd963ce" />

9. "Add" a Bibtex export.  
<img width="293" alt="Screenshot 2025-05-23 at 15 43 07" src="https://github.com/user-attachments/assets/1181d66b-db91-4cf1-8e80-da5e56529bae" />

> Source - select either your entire library or a folder.  
> Destination - select Github.
> Repository - you can either type this or copy the link from the "Code" button in your repository.  
> Branch - you can leave this blank if you're using _main_.  
> Path - this can be ```references.bib``` if you want the file within the same folder, or you can nest it into a folder like so ```folder/references.bib```. Don't make my mistake of typing out your whole path and nesting multiple folders within your folder. And creating two references.bib files. Which then return errors and make you very confused and give you another headache. The file will be automatically created by Paperpile so you don't need to create a blank one in your folder.  
<img width="682" alt="Screenshot 2025-05-23 at 15 47 52" src="https://github.com/user-attachments/assets/5c8e5d15-f5f3-4548-aabe-6a328e952792" />

10. Add Paperpile-bot as a collaborator.  
<img width="671" alt="Screenshot 2025-05-23 at 15 55 28" src="https://github.com/user-attachments/assets/cbc912e8-5a5d-467f-a03e-3ffb1bcd3600" />

11. Once this has loaded, you should see that Paperpile-bot has created a references.bib file in your repository! Success!! Hopefully!
(Yours should be a few minutes ago rather than the 2h shown in my screenshot.)    
<img width="1093" alt="Screenshot 2025-05-23 at 15 56 48" src="https://github.com/user-attachments/assets/643e9ac7-3acb-45df-9ef4-2841734372ad" />

### Okay, so now you should have all 3 elements:
1. A Notion page with a database and an Integration which has access to the page (should have been in the Notion Integration tutorial!).
2. A Github page that's up-to-date, as well as your main coding files - _newpage.json_, _paperpile_api.py_ and _notion_api.py_.
4. A _references.bib_ file in your Github produced by the Paperpile Bibtex export.  

#### Now to the last part! Where it hopefully all comes together! 
12. ```Pull``` your new references.bib file from Github. To do this, use ```git pull origin main``` in Terminal. 

13. Run ```python3 paperpile_api.py```. This should show at the end "X entries successfully added to Notion!" and you should also see these entries in your Notion table. If you're getting errors, I'm sorry and godspeed on your debugging journey. It means I was not able to save you from the headaches. If it worked, then yay!! 

#### Whenever you add new references to Paperpile, the _references.bib_ file will be automatically updated in your Github (you will be able to see this in the _Commits_ as 'Paperpile-bot updated references.bib'. However, this does not carry into updating your Notion. I'm sure someone with actual Computer Science knowledge would be able to do this somehow but for now, you get this because a tired biologist wrote it instead. 

14. To update your Notion database, you will need to ```pull``` the new references.bib file and then run ```python3 paperpile_api.py``` again. 

Notes and disclaimer!
- I am not a programmer! My degree is in human biology, so don't be mean. I only wrote this because I didn't want to manually type all my Paperpile references I had and I couldn't find anything functional online. 
- This was done with aggressive debugging using chatGPT - it seems to be working and I've been able to update it but I'm not going to pretend I wrote it from scratch or that I know what I'm doing.
- Be careful pressing tab vs space as you can get indentation errors.
- Make sure you stay up to date with github and the directionality, as it can be a bit of a nightmare otherwise.
