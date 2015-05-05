package com.funshion.artemis.recommend;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.List;

import org.apache.mahout.cf.taste.impl.common.LongPrimitiveIterator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.recommender.CachingRecommender;
import org.apache.mahout.cf.taste.impl.recommender.slopeone.SlopeOneRecommender;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        for(int i = 0; i < args.length; i++)
        {
        	System.out.println(args[i]);
        }
        String inputFile = args[0];
        String outputFile = args[1];
        App app = new App();
        app.creatCSVFile(inputFile, outputFile);
        //根据csv文件创建模型
        File csvFile = new File(outputFile);
        try {
			FileDataModel model = new FileDataModel(csvFile);
			CachingRecommender cr = new CachingRecommender(
					new SlopeOneRecommender(model));
			for(LongPrimitiveIterator it = model.getUserIDs(); it.hasNext();)
			{
				long userId = it.nextLong();
				List<RecommendedItem> recommendations = cr.recommend(userId, 10);
				for(RecommendedItem item : recommendations)
				{
					System.out.println("User: " + userId + "\t" + item);
				}
			}
		} catch (Exception e){
			e.printStackTrace();
		}
        
    }
    public void creatCSVFile(String input, String output)
    {
    	try {
			BufferedReader br = new BufferedReader(new FileReader(input));
			BufferedWriter bw = new BufferedWriter(new FileWriter(output));
			String[] tmp;
			String line;
			int i = 0;
			while((line = br.readLine()) != null && i < 10000)
			{
				i++;
				tmp = line.trim().split("::");
				bw.write(tmp[0] + "," + tmp[1]);
				bw.newLine();
				bw.flush();
			}
			bw.close();
			br.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
    	
    }
}
