package godknows.schoolpubliccomment;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import java.util.LinkedList;
import java.util.List;
/**the MyFavorite activity
  created by liv4evr
  after clicking the button"我的收藏", we'll get to this activity to see all the stores we've made favorite.
  intended that in this activity all the favorites are listed here, and we have access to all favorites through this activity
*/
public class MyFavorites extends AppCompatActivity {

    private List<FavoriteDisplay> favorlist=null;
    private Context mContext;
    private FavoriteDisplayAdapter ad;
    private ListView list_favoritedisplay;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_favorites);
        mContext=MyFavorites.this;
        list_favoritedisplay=(ListView)findViewById(R.id.displayFavorites);
        favorlist=new LinkedList<FavoriteDisplay>();
        favorlist.add(new FavoriteDisplay("Sample1",4.3,R.drawable.heart_72px));
        favorlist.add(new FavoriteDisplay("Sample2",4.5,R.drawable.heart_72px));
        favorlist.add(new FavoriteDisplay("Sample3",3.8,R.drawable.heart_72px));
        favorlist.add(new FavoriteDisplay("Sample4",4.9,R.drawable.heart_72px));
        ad=new FavoriteDisplayAdapter((LinkedList<FavoriteDisplay>) favorlist,mContext);
        list_favoritedisplay.setAdapter(ad);
        list_favoritedisplay.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
                Intent it=new Intent(MyFavorites.this,storeInfo.class);
                String snm=parent.getItemAtPosition(position).getClass().getName();//I'm still in doubt how to get the clicked item in the listview, perhaps this line leads to an error.
                Bundle bd=new Bundle();
                bd.putString("storeName",snm);
                it.putExtras(bd);
                startActivity(it);
            }
        });
    }

}
