package godknows.schoolpubliccomment;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
/**User center activity
  created by liv4evr
  the user center of school public comment
  from this activity we can get to several individual windows, such as my settings and my favorites
  and from this activity we can terminate this app by clicking the red button below.
 */
public class UserCenter extends AppCompatActivity {
private Button btCourses,btFavors,btRatings,btSettings,btExit;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_center);
        btCourses=(Button)findViewById(R.id.buttonForMyCourses);
        btCourses.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(UserCenter.this,MyCourses.class);
                startActivity(it);
            }
        });
        btFavors=(Button)findViewById(R.id.buttonForMyFavorites);
        btFavors.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent it=new Intent(UserCenter.this,MyFavorites.class);
                startActivity(it);
            }
        });
        btRatings=(Button)findViewById(R.id.buttonForMyRatings);
        btRatings.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(UserCenter.this,MyRatings.class);
                startActivity(it);
            }
        });
        btSettings=(Button)findViewById(R.id.buttonForMySettings);
        btSettings.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(UserCenter.this,MySettings.class);
                startActivity(it);
            }
        });
        btExit=(Button)findViewById(R.id.buttonForExit);
        btExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

    }
}
