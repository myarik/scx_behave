Feature: Blog parsing

  Scenario: jessiibrownie
    When I visit url https://jessiibrownie.wordpress.com/2016/01/29/a-day-in-agua-blanca/ in file jessiibrownie.html
    Then I should see Last weekend I spent the Sunday out with the family
    Then I should see I know is a little different to what I usually post but
    And I should not see November 2013
    And I should not see ABOUT ME
    And I should not see Looks like a cool place

  Scenario: bellamorous
    When I visit url http://bellamorous.blogspot.com/2016/02/life-college.html in file bellamorous.html
    Then I should see Due to that I show you this total
    And I should see I decided to buy this pant skirt or culotte because
    And I should see SEE YOU SOON
    And I should not see Besos... Carli
    And I should not see ABOUT ME
    And I should not see BLOG ARCHIVES

  Scenario: shefinds
    When I visit url http://www.shefinds.com/2016/5-ways-to-make-the-most-of-the-money-talk-adultlife/ in file shefinds.html
    Then I should see Now before you book a boardroom
    And I should see clear financial roles and expectations
    And I should see he mistaken double charge at the grocery store
    And I should not see subscribe
    And I should not see kids
    And I should not see comments

  Scenario: thesmallthingsblog
    When I visit url http://www.thesmallthingsblog.com/2016/02/1-braid-2-ways-to-finish-the-style/ in file thesmallthingsblog.html
    Then I should see hair grow 10 inches
    And I should see messy bun on the opposite side
    And I should see if you post a pic
    And I should not see email address
    And I should not see baby
    And I should not see FAQ

  Scenario: extrapetite
    When I visit url http://www.extrapetite.com/2016/01/snow-day.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+ExtraPetite+%28Extra+Petite%29 in file extrapetite.html
    Then I should see Snow day
    And I should see Jonas stayed safe
    And I should see video tutorial sometime!
    And I should not see the mittens and the hat to match
    And I should not see Notify me
    And I should not see haha

  Scenario: thechrisellefactor
  When I visit url http://thechrisellefactor.com/2016/01/5-apps-to-be-more-productive-in-2016/ in file thechrisellefactor.html
  Then I should see tips
  And I should see Google Calendar
  And I should see Share some of your tips
  And I should not see haha
  And I should not see Comments are closed
  And I should not see search
  And I should not see lifestyle


 Scenario: thesmallthingsblog2
  When I visit url http://www.thesmallthingsblog.com/2016/01/the-coffee-bar/ in file thesmallthingsblog2.html
  Then I should see The coffee bar
  And I should see David’s old nursery
  And I should see an entire room dedicated solely to coffee
  And I should not see Required fields are marked
  And I should not see follow-up comments by email.
  And I should not see haha

 Scenario:beautezine
   When I visit url http://www.beautezine.com/brighten-tired-eyes-clinique-pep-start/ in file beautezine.html
   Then I should see SPONSORED BY CLINIQUE
   And I should see Don’t forget to
   And I should see Dark circles, puffiness and fine lines
   And I should not see PRODUCT OF THE DAY
   And I should not see haha
   And I should not see You Might Also Like

Scenario:urbanette
   When I visit url http://urbanette.com/lose-those-winter-blues-and-blahs/ in file urbanette.html
   Then I should see  Weekend section of the New York Times
   And I should see When all else fails and the winter blues persist
   And I should see Find a tai chi class
   And I should not see haha
   And I should not see CONNECT WITH US!
   And I should not see ENTER YOUR EMAIL BELOW


















