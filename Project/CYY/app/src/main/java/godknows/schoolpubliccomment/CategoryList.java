package godknows.schoolpubliccomment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;

import org.apache.http.params.CoreConnectionPNames;

import java.util.LinkedList;
import java.util.List;

import static java.net.Proxy.Type.HTTP;

public class CategoryList extends AppCompatActivity {

    private List<FavoriteDisplay> showlist=null;
    private Context mContext;
    private FavoriteDisplayAdapter ad;
    private ListView list_categorydisplay;
    private TextView title;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_category_list);
        Intent it=getIntent();
        Bundle bd=it.getExtras();
        String ctg=bd.getString("category");
        title=(TextView)findViewById(R.id.categoryName);
        title.setText(ctg);
        String apdix="";
        switch(ctg)
        {
            case "caterings" : apdix="merchant";
            case "entertainments" : apdix="fun";
            case "courses" : apdix="course";
            case "others" : apdix="other";
        }
        String url="123.206.106.24:8000/"+apdix;
        //get JSON
        String res=doPost(,url);
        //parse JSON
        mContext=CategoryList.this;
        list_categorydisplay=(ListView)findViewById(R.id.categoryListView);
        showlist=new LinkedList<FavoriteDisplay>();
        //add
        ad=new FavoriteDisplayAdapter((LinkedList<FavoriteDisplay>) showlist,mContext);
        list_categorydisplay.setAdapter(ad);
        //on click listener
        list_categorydisplay.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
                Intent it=new Intent(CategoryList.this,storeInfo.class);
                String snm=parent.getItemAtPosition(position).getClass().getName();
                Bundle bd=new Bundle();
                bd.putString("storeName",snm);
                it.putExtras(bd);
                startActivity(it);
            }
        });
    }
    /*public void parseJson(List l,String j)
    {

    }*/
    public static String doPost(List<NameValuePair> params, String url)
            throws Exception {
        String result = null;
        HttpClient httpClient = new DefaultHttpClient();
        HttpPost httpPost = new HttpPost(url);
        if (params != null)
        {    HttpEntity entity = new UrlEncodedFormEntity(params, HTTP.UTF_8);
            httpPost.setEntity(entity);
        }
        httpClient.getParams().setParameter(CoreConnectionPNames.CONNECTION_TIMEOUT, 3000);
        httpClient.getParams().setParameter(CoreConnectionPNames.SO_TIMEOUT, 3000);
        HttpResponse httpResp = httpClient.execute(httpPost);
        if (httpResp.getStatusLine().getStatusCode() == 200) {
            result = EntityUtils.toString(httpResp.getEntity(), "UTF-8");
        } else {
            Log.i("HttpPost", "HttpPost方式请求失败");
        }
        return result;
    }
}
