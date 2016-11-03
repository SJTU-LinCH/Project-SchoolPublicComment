package godknows.schoolpubliccomment;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
/** the storeinfo activity
 created by liv4evr
 just a token used by my other activities ,such as MyFavorites.
 when collaborator's part is completed, this file ought to be replaced.
 */
public class storeInfo extends AppCompatActivity {

    private TextView nm;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_store_info);
        Intent itn=getIntent();
        Bundle bdn=itn.getExtras();
        String nameOfStore=bdn.getString("storeName");
        nm=(TextView)findViewById(R.id.StoreName);
        nm.setText(nameOfStore);
    }
}
