package godknows.schoolpubliccomment;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
/**the MyCourses activity
  created by liv4evr
  after clicking the button"我的课程", we'll get to this activity to see all the courses we‘ve taken in this semester.
  intended to make it look like a schedule, but I haven't done it.
*/
public class MyCourses extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_courses);
    }
}
