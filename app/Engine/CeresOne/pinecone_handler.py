import pinecone




# Initialize Pinecone
pinecone.init(api_key="e26c7676-bc1f-42e3-8071-5d14948de64f", environment="us-west1-gcp-free")

# Specify your index name and dimension



index = pinecone.Index("pathways")

# Define the vector to insert


vid = "UCLA"

vector = [1, 1, 2023 ,0.04260563850402832, 0.02487262338399887, 0.040468692779541016, 0.024373706430196762, 0.00932021252810955,
       0.05310455709695816, 0.008075275458395481, 0.03944757580757141, 0.03545476123690605, 0.04227662459015846,
       0.04154672473669052, 0.022037938237190247, 0.332561194896698, 0.0357113778591156, 0.014026730321347713,
       0.025990569964051247, 0.008277936838567257, 0.00837161298841238, 0.038606543093919754, 0.013856294564902782,
       0.005954570136964321, 0.015879742801189423, 0.03434615209698677, 0.01153059583157301, 0.008915749378502369,
       0.00361251225695014, 0.020532898604869843, 0.032227564603090286, 0.009509364143013954, 0.017359182238578796,
       0.004261330235749483, 0.003955957014113665, 0.002311341231688857, 0.003006884129717946, 0.06254571676254272,
       0.024868717417120934, 0.01553208939731121, 0.007407883647829294, 0.012863296084105968, 0.018209660425782204,
       0.07056757807731628, 0.005836810916662216, 0.010188078507781029, 0.013345045037567616, 0.017294762656092644,
       0.03740997985005379, 0.017423925921320915, 0.010608848184347153, 0.12458518147468567, 0.11128753423690796,
       0.004285026807337999, 0.019687900319695473, 0.01938880980014801]



index.upsert([
    (vid, vector),
])

def retrieve_all_vectors(index_name):
    pinecone.init(api_key="e26c7676-bc1f-42e3-8071-5d14948de64f", environment="us-west1-gcp-free")

    index_info = pinecone.list_indexes()

    if index_name not in index_info.index_names:
        raise ValueError(f"Index '{index_name}' does not exist")

    query_results = pinecone.query_index(index_name=index_name, query_vectors=None)

    vectors = query_results.vectors

    pinecone.deinit()

    return vectors



