# Customer Questions for Lab on 2/18/19

1. Moving forward, should we focus on the CLI or should we be working
  toward a web interface?

  End goal is the web interface (simple, sreamlit). Part of our job is to
  control the scope.

2. Does the user prefer to use the tool by typing a long command of parameters, inputs, and arguments?

3. Does the customer want a program with a fixed output, or a personalized output?

  - has had experience that interactive prompting is difficult to reproduce
    this
  - save history and do fuzzy search, match to command line arguements
  - reuse is easir when specified in the command Line
  - the tool should have a way to say here are simple prompts them template output
  - cool: run tool, specifies and full report in CLI , then an option to
    click link and interact in the browser and links brings it to a Streamlit
    interface (minimal command line arguements)

4. "Easier" is open to interpretation - each tool runs standalone but can
  run into another tools

5. Other people have done hybrid of ask and wait but this is adds complexity
  - looping through ask/questions is not needed here - use web interface
  applications instead and allow only one parameter can be changed rather
  than looping through them all
  - link to localhost the jumps to streamlit and link passes along what was
  typed in command line then visualizes
  - interactivity wth graphs exclusively in the browser rather than in CLI

6. Should be put the hosted website remote or local?

  - local for feasability 
