// JSON pretty formatting example
// This example can only handle UTF-8. For handling other encodings, see prettyauto example.

#include "rapidjson/reader.h"
#include "rapidjson/prettywriter.h"
#include "rapidjson/filereadstream.h"
#include "rapidjson/filewritestream.h"
#include "rapidjson/error/en.h"

using namespace rapidjson;



#if defined(BUILD_MONOLITHIC)
#define main(c, a)			Rjson_example_pretty_main(c, a)
#endif

int main(int argc, const char** argv)
{
    // Prepare reader and input stream.
    Reader reader;
    char readBuffer[65536];
    FileReadStream is(stdin, readBuffer, sizeof(readBuffer));

    // Prepare writer and output stream.
    char writeBuffer[65536];
    FileWriteStream os(stdout, writeBuffer, sizeof(writeBuffer));
    PrettyWriter<FileWriteStream> writer(os);

    // JSON reader parse from the input stream and let writer generate the output.
    if (!reader.Parse<kParseValidateEncodingFlag>(is, writer)) {
        fprintf(stderr, "\nError(%u): %s\n", static_cast<unsigned>(reader.GetErrorOffset()), GetParseError_En(reader.GetParseErrorCode()));
        return 1;
    }

    return 0;
}
