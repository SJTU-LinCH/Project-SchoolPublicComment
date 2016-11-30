package godknows.schoolpubliccomment;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class HomePage extends AppCompatActivity {
    private Button btCaterings,btEntertainments,btCourses,btOthers,testerButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);
        btCourses=(Button)findViewById(R.id.buttonForCourses);
        /**
         * click on the button and send the name of the category user wants to acquire
         */
        btCourses.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(HomePage.this,CategoryList.class);
                Bundle bd=new Bundle();
                bd.putString("Category","courses");
                it.putExtras(bd);
                startActivity(it);
            }
        });
        btCaterings=(Button)findViewById(R.id.buttonForCaterings);
        btCaterings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent it=new Intent(HomePage.this,CategoryList.class);
                Bundle bd=new Bundle();
                bd.putString("Category","caterings");
                it.putExtras(bd);
                startActivity(it);
            }
        });
        btEntertainments=(Button)findViewById(R.id.buttonForEntertainments);
        btEntertainments.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(HomePage.this,CategoryList.class);
                Bundle bd=new Bundle();
                bd.putString("Category","entertainments");
                it.putExtras(bd);
                startActivity(it);
            }
        });
        btOthers=(Button)findViewById(R.id.buttonForOthers);
        btOthers.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(HomePage.this,CategoryList.class);
                Bundle bd=new Bundle();
                bd.putString("Category","others");
                it.putExtras(bd);
                startActivity(it);
            }
        });
        testerButton=(Button)findViewById(R.id.tester);
        testerButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent it=new Intent(HomePage.this,UserCenter.class);
                startActivity(it);
            }
        });
    }
}
