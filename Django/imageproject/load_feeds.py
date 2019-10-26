import sys, os 
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imageproject.settings')

import django
django.setup()

from reco.models import Feed


def save_feed_from_row(feed_row):
    feed = Feed()
    feed.id = feed_row[0]
    feed.name = feed_row[1]
    feed.price = feed_row[2]
    feed.text = feed_row[3]
    feed.image = feed_row[4]
    feed.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:

        print ("Reading from file " + str(sys.argv[1]))
        feeds_df = pd.read_csv(sys.argv[1], encoding='CP949')
        print (feeds_df)

        feeds_df.apply(
            save_feed_from_row,
            axis=1
        )

        print ("There are {} feeds".format(Feed.objects.count()))
        
    else:
        print ("Please, provide feed file path")
