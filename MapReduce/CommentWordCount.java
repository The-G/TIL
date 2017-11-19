package com.tt;

import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Map;

import mrdp.utils.MRDPUtils;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import org.apache.commons.lang.StringEscapeUtils;

public class CommentWordCount {
	public static class WordCountMapper extends Mapper<Object, Text, Text, IntWritable> {
		private static IntWritable one = new IntWritable(1);
		private org.w3c.dom.Text word = new Text();
		
		public void map(Object key, javax.xml.soap.Text value, Context context) throws IOException, InterruptedException {
			
			// Parse the input string into a nice map
			// static이라 바로 가져다 씀
			Map<String, String> parsed = MRDPUtils.transformXmlToMap(value.toString());

			// Grab the "Text" field, since that is what we are counting over
			String txt = parsed.get("Text");
			
			// .get will return null if the key is not there
			if (txt == null) {
				// skip this record
				return;
			}
			
			// Unescape the HTML because the SO data is escaped. html code가 있을까봐!!
			txt = StringEscapeUtils.unescapHtml(txt.toLowerCase());
			
			// Remove some annoying punctuation
			txt = txt.replaceAll("'", ""); // remove single quotes (e.g., can't)
			txt = txt.replace("[^a-zA-Z]", " "); // replace the rest with a space 영문자가 아닌것은 space로 변경!
			
			// Tokenize the string, then send the tokens away
			StringTokenizer itr = new StringTokenizer(txt);
			while (itr.hasMoreTokens()) {
				word.setData(itr.nextToken());
				context.write(word, one);
			}
		}
	}
	
	public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
		private IntWritable result = new IntWritable();
		
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}		
			reuslt.set(sum);
			context.write(key, result);
		}
	}
	
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();

	    // 나중에 AWS 할 때 이부분을 잘 수정하면 된다!! pem키를 이용해서 connect 해야하는데!!!
		conf.set("fs.default.name", "hdfs://192.168.00.108:9000");
		conf.set("mapred.job.tracker", "192.168.00.108:9001");
		conf.set("mapred.jar","C:/dev/workspace/mr.jar");

		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		
		if (otherArgs.length != 2) {
			System.err.println("Usage: CommentWordCount <in> <out>");
			System.exit(2);	
		}
		
		Job job = new Job(conf, "StrackOverflow Comment Word Count");
		job.setJarByClass(CommentWordCount.class);
		job.setMapperClass(SOWordCountMapper.class);
		job.setCombinerClass(IntSumReducer.class);
		job.setReducerClass(IntSumReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}

/*
	~ C:/dev/workspace/mr.jar 파일 생성
	
	~ 프로그램 아규먼트 설정 : /user/stackexchange /user/stackoutput1
	
	~ 실행 및 결과 확인
	
	~ R을 활용한 워드클라우드 
	
	~ 위 실습 관련 설명 부족하다. 
	http://kjhgao.tistory.com/admin/entry/post/?id=62&type=post&returnURL=%2Fmanage%2Fposts
	참고, 정리도 해야하고!! 
*/
