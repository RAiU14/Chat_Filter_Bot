# Chat Filter Bot
### A Chat filteration bot for Discord servers.   
###### V : 3.1.1
Concept : There are certain ban words within different servers, of course there are many other bots that does word filteration throughout texts but there are certain times when the bot cannot understand fancy combinations of the same word. The goal of this bot is to filter out any combinations of these words. 

### Syntax : &
>Custom syntax changing as per server's settings are not yet available.


###What the bot does as of now:
- Add/Remove words to the filter list.
- Add/Remove words to ignore list.
- Check or view if the word is present in the filter list.
- View the contents of ignore list.
- Monitor words sent to the server and deletes word if there is a banned word in the message.
  - Words sent on ignored channels or by the user having the role will not have their message deleted.
  - Additionally, the bot mentions/tags the user about bannned word usage.


### Available commands to the date - 
- **&wfilter** : To display all the contents in the filter list.  
Usage: `&wfilter`  
- **&wfadd** : To add a new word to the list.  
Usage: `&wfadd` word  
You have to always mention a word to be added in the filter list.  
- **&wfdelete** : To delete a word from the list.  
Usage: `&wfadd` word  
You have to mention the word which is present in the filter list so that it can be deleted.  
- **&wfclear** : To clear the complete filter list.  
Usage: `&wfclear`  
- **&ichadd** : To add a channel to ignore list.  
Usage: `&ichadd` #channel-name  
You have to always mention the channel name, or even pass a list of channels you want to add to ignore list. You cannot type the channel name.  
If you are not mentioning the channel name, the bot will add the current channel (where the command was triggered from) to ignore list.
- **&ichdel**: To delete a channel from ignore list.  
Usage: `&ichdel` #channel-name  
You have to always mention the channel name, or even pass a list of channels you want to delte that channel from ignore list. You cannot type the channel name.  
If you are not mentioning the channel name, the bot will delete the current channel (where the command was triggered from) from ignore list. 
- **&iradd**: To add a role to ignore list.  
Usage: `&iradd` @Role-name  
You have to mention the role or a list of roles to be added in ignore list. Not mentioning role will result in an error and the command have to be reused again.  
You cannot type the role name, rather have to mention the role or a list of role. 
- **&irdel**: To delete a role from ignore list.  
- Usage: `&irdel` @Role-name  
You have to mention the role or a list of roles to be deleted from ignore list. Not mentioning role will result in an error and the command have to be reused again.  
You cannot type the role name, rather have to mention the role or a list of role. 
- **&igview**: To view the complete contents of ignore list.  
Usage: `&igview` channel/view  
You have to mention the parameter if the list to be displayed is `channel` or `roles`. 

  
> 🚧 Work in Progress 🚧 
>- Delete all the commands used by the user once the resulting message is "True." or "Successful!"
>- Feature where only users with admin powers or roles with admin powers or powers such as `Manage Messages` can trigger commands excluding view commands.   
>>###Further enhancement -
>>- On reaction; delete a certain message sent by the bot.   
>>- A "Beta Tester Role" to edit these special character's dictionary.

>>>🛑**Development Temporarily Halted**🛑