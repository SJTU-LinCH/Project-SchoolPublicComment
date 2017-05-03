package godknows.schoolpubliccomment;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.LinkedList;


/**favoriteDisplayAdapter class
created by liv4evr
used in MyFavorites activity to contain the favorites displayed in this activity, and may be used in other's activity.
using viewHolder to optimize the loading of views
 */
public class FavoriteDisplayAdapter extends BaseAdapter{
    private LinkedList<FavoriteDisplay> data;
    private Context mContext;
    public FavoriteDisplayAdapter(LinkedList<FavoriteDisplay> lst,Context mtxt){
        this.data=lst;
        this.mContext=mtxt;
    }
    @Override
    public int getCount()
    {
         return data.size();
    }
    @Override
    public Object getItem(int position) {return null;}
    @Override
    public long getItemId(int position) {return position;}
    @Override
    public View getView(int position, View convertView, ViewGroup parent)
    {
        ViewHolder holder =null;
        if(convertView==null) {
            convertView=LayoutInflater.from(mContext).inflate(R.layout.favoritedisplaylayout,parent,false);
            holder= new ViewHolder();
            holder.img_icon=(ImageView) convertView.findViewById(R.id.StoreIcon);
            holder.txt_name=(TextView) convertView.findViewById(R.id.StoreName);
            holder.num_score=(TextView) convertView.findViewById(R.id.StoreScore);
            convertView.setTag(holder);}
        else {holder=(ViewHolder)convertView.getTag();}
        holder.img_icon.setBackgroundResource(data.get(position).getIcon());
        holder.num_score.setText(data.get(position).getScore());
        holder.txt_name.setText(data.get(position).getName());
        return convertView;
    }
    static class ViewHolder
    {
        ImageView img_icon;
        TextView txt_name;
        TextView num_score;
    }
}
