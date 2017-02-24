#include<string>
#include<vector>

using namespace std;

namespace data_struct
{

struct Data
{
   char id;

} Entry;


class Trie
{
    public:
	const char ID
	Trie(const char& ID);
	Data* get_data(string& name);
	bool store_data(string& data);

    private:
	vector<Trie> tries;
	vector<Data> data_list;
	

};
}

