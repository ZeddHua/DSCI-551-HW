import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class SQL2MR {
	
	public static class MyMapper extends Mapper<Object, Text, Text, FloatWritable>{
		
		@Override
		protected void map(Object offset, Text rows, Context context) throws IOException, InterruptedException{
			
			String values = rows.toString();
			StringTokenizer cols = new StringTokenizer(values, "\t");
						
			if (cols.hasMoreTokens()){
				String col0 = cols.nextToken();
				String col1 = cols.nextToken();
				String col2 = cols.nextToken();
				String col3 = cols.nextToken();
				
				if (Integer.parseInt(col2)>=60){				
				context.write(new Text(col3),new FloatWritable(Float.parseFloat(col1)));
				}
			}
		}
	}
	
	public static class MyReducer extends Reducer <Text, FloatWritable, Text, FloatWritable>{
		float sum = 0;
		float avg = 0;
		int i = 0;
		@Override
		protected void reduce (Text rating, Iterable<FloatWritable> rental_rates, Context context ) 
			throws IOException, InterruptedException {
				//Map<String, Float> statInfo = getSum(rental_rates);
				
				for (FloatWritable rental_rate : rental_rates){
					sum+= rental_rate.get();
					i ++;
				}
				if (i >=160){
					context.write(rating, new FloatWritable(sum/i));
				}
		}
	}
	
	public static void main(String[] args) throws Exception{
		
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		for ( int i = 0; i< otherArgs.length; ++i){
			System.out.println(otherArgs[i]);
		}
		Job job = Job.getInstance(conf, "hw5");
		job.setJarByClass(SQL2MR.class);
		job.setMapperClass(MyMapper.class);
		job.setReducerClass(MyReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(FloatWritable.class);
		
		for (int i = 0; i< otherArgs.length -1 ; ++i){	
			FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
		}
		
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[otherArgs.length -1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
		
}



