### Names of variables
This file provide description to the variable names created in `fetch_trending` script. The variable collected can be used as an indications of why it was on trending to begin with. 

>1. **ID**: unique identifier for the video. It is extracted as the root of the link of the video. The actual link to the video is 
>
>   ```python
>   'https://www.youtube.com/watch?v=' + ID
>   ```
>
>2. **timestamp**: time of when the information was collected. 
>3. **title**: title of the video
>4. **description**: description of the video. 
>5. **Verified**: checks if the channel is verified/official
>6. **viewcount**: number of views of the video 
>7. **channel_name**: name of the youtube channel
>8. **date_uploaded**: when was the video uploaded 
>9. **likes**: number of likes of the video 
>10. **dislikes**: number of dislikes of the video
>11. **comments**: number of comments on the video 
>12. **upvotes**: total number of likes on all the comments 
>13. **downvotes**: total number of dislikes on all of the comments 
>14. **ranks**: youtubes ranking of the video. The first video is rank 1 with the hashtag '#1 on trending'
>
>

### Retrieval Method

Most of the data was obtained using a css selector. However, this method does not work with buttons. The number of likes and dislikes for example is embedded in a button on which you can click to increase its value. The actual number is stored in the `arial-label` section of a `button` tag. After some exploration, the number of like and number of dislikes are on the 18$^\text{th}$ and the 20$^\text{th}$ button.  

**steps**

1. hover over the element you want to scrape and right click on it . 
2. go to inspect elements
3. this will take you to the corresponding html tag for this element 
4. then right click on the html tag and copy as CSS SELECTOR

### Issues

Comments counts seem more dynamic. Waiting times of up to 1000 seconds seems insufficient. We might have to write a separate script for comments.