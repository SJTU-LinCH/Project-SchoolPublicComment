package godknows.schoolpubliccomment;


/**favoriteDisplay claas
created by liv4evr
a class which contains all the things we show in a listview in some certain activity of a store
 */
public class FavoriteDisplay {
    int icon;
    String name;
    double score;
    public FavoriteDisplay(){
    }
    public FavoriteDisplay(String nm,double sc,int ic) {
        this.icon=ic;
        this.name=nm;
        this.score=sc;
    }
    public int getIcon(){
        return this.icon;
    }
    public String getScore(){
        return Double.toString(this.score);
    }
    public String getName(){
        return this.name;
    }
    public void setIcon(int ic){
        this.icon=ic;
    }
    public void setName(String nm){
        this.name=nm;
    }
    public void setScore(int sc){
        this.score=sc;
    }

}
