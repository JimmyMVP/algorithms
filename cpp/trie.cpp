#include "trie.hpp"


namespace data_struct
{


    Trie::Trie(const char& ID){this->ID(ID)}
    {}

Entry* Trie::get_data(string& name)
{
    if(name.size() > 1)
	return get_data(name.substr(1))
    else
	for(Entry e : data_list)
	{
	    if(e.id == name[0])
		return e
	}

    return 0;
}
bool Trie::store_data(string& name)
{
    
    return false;
}

}

