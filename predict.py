


<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>NeverWork/predict.py at master from stepleon/NeverWork - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="XxBEIYwab8+9vnZQkquB9S+DhRbUlPps8j6gY1VCnoM=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundles/github-0f7a38f35ff5c3fd433bfe7e85fe43e804d7df70.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/jquery-e46225f266eba00902b2e5b66fe6fe6a484fb242.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundles/github-6a5b4de8446db50cd6e1b8e1c0dce6dfd07ba8f6.js" type="text/javascript"></script>
    

      <link rel='permalink' href='/stepleon/NeverWork/blob/7423e2a31bd6ffd7ed4879e65a7291dab858615d/NeverWork/predict.py'>

    <meta name="description" content="NeverWork hosted on GitHub" />
  <link href="https://github.com/stepleon/NeverWork/commits/master.atom?login=ccubed510&token=16bb97903003771c044358bc7c90ba02" rel="alternate" title="Recent Commits to NeverWork:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob windows vis-private env-production ">
    


    

      <div id="header" class="true clearfix">
        <div class="container clearfix">
          <a class="site-logo" href="https://github.com/">
            <!--[if IE]>
            <img alt="GitHub" class="github-logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7.png?1323882770" />
            <img alt="GitHub" class="github-logo-hover" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7-hover.png?1324325405" />
            <![endif]-->
            <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1323882770" />
            <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1324325405" />
          </a>

              
    <div class="topsearch ">
<form action="/search" id="top_search_form" method="get">        <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
        <div class="search placeholder-field js-placeholder-field">
          <label class="placeholder" for="global-search-field">Search…</label>
          <input type="text" class="search my_repos_autocompleter" id="global-search-field" name="q" results="5" /> <input type="submit" value="Search" class="button" />
        </div>
        <input type="hidden" name="type" value="Everything" />
        <input type="hidden" name="repo" value="" />
        <input type="hidden" name="langOverride" value="" />
        <input type="hidden" name="start_value" value="1" />
</form>      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore</a></li>
          <li><a href="https://gist.github.com">Gist</a></li>
          <li><a href="/blog">Blog</a></li>
        <li><a href="http://help.github.com">Help</a></li>
      </ul>
    </div>


            


  <div id="userbox">
    <div id="user">
      <a href="https://github.com/ccubed510"><img height="20" src="https://secure.gravatar.com/avatar/67c4f0da7fbf2c28af835e2a917f2895?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="20" /></a>
      <a href="https://github.com/ccubed510" class="name">ccubed510</a>
    </div>
    <ul id="user-links">
      <li>
        <a href="/inbox/notifications" id="notifications" class="tooltipped downwards" title="Notifications">
          <span class="icon">Notifications</span>
        </a>
      </li>
      <li><a href="/account" id="settings" class="tooltipped downwards" title="Account Settings"><span class="icon">Account Settings</span></a></li>
      <li><a href="/logout" id="logout" class="tooltipped downwards" title="Log Out"><span class="icon">Log Out</span></a></li>
    </ul>
  </div>



          
        </div>
      </div>

      

            <div class="site">
      <div class="container">
        <div class="pagehead repohead instapaper_ignore readability-menu">


        <div class="title-actions-bar">
          <h1>
            <a href="/stepleon">stepleon</a> /
            <strong><a href="/stepleon/NeverWork" class="js-current-repository">NeverWork</a></strong>
          </h1>
          



              <ul class="pagehead-actions">


          <li class="js-toggler-container watch-button-container ">
            <a href="/stepleon/NeverWork/toggle_watch" class="minibutton btn-watch watch-button js-toggler-target" data-method="post" data-remote="true" rel="nofollow"><span><span class="icon"></span>Watch</span></a>
            <a href="/stepleon/NeverWork/toggle_watch" class="minibutton btn-watch unwatch-button js-toggler-target" data-method="post" data-remote="true" rel="nofollow"><span><span class="icon"></span>Unwatch</span></a>
          </li>

              <li><a href="/stepleon/NeverWork/fork" class="minibutton btn-fork fork-button" data-method="post" rel="nofollow"><span><span class="icon"></span>Fork</span></a></li>

              <li class="nspr">
                <a href="/stepleon/NeverWork/pull/new/master" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a>
              </li>


      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers ">
            <a href="/stepleon/NeverWork/watchers" title="Watchers" class="tooltipped downwards">
              1
            </a>
          </li>
          <li class="forks">
            <a href="/stepleon/NeverWork/network" title="Forks" class="tooltipped downwards">
              1
            </a>
          </li>
        </ul>
      </li>
    </ul>

        </div>

          

  <ul class="tabs">
    <li><a href="/stepleon/NeverWork" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/stepleon/NeverWork/network" highlight="repo_networkrepo_fork_queue">Network</a>
    <li><a href="/stepleon/NeverWork/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/stepleon/NeverWork/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/stepleon/NeverWork/wiki" highlight="repo_wiki">Wiki <span class='counter'>0</span></a></li>

    <li><a href="/stepleon/NeverWork/graphs" highlight="repo_graphsrepo_contributors">Stats &amp; Graphs</a></li>

  </ul>

  
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/stepleon/NeverWork/tree-list/7423e2a31bd6ffd7ed4879e65a7291dab858615d"
      data-blob-url-prefix="/stepleon/NeverWork/blob/7423e2a31bd6ffd7ed4879e65a7291dab858615d"
    >

  <div class="breadcrumb">
    <b><a href="/stepleon/NeverWork">NeverWork</a></b> /
    <input class="tree-finder-input js-navigation-enable" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/stepleon/NeverWork/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever" rel="nofollow">Dismiss</a>
        <strong>Octotip:</strong> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list js-navigation-container" data-navigation-enable-mouse>
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form>
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        <span>Go</span>
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions subnav">
    <li><a href="/stepleon/NeverWork/tags" class="blank" highlight="repo_tags">Tags <span class="counter">0</span></a></li>
    <li><a href="/stepleon/NeverWork/downloads" class="blank downloads-blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
    
  <li class="search repo-search ">
<form action="/stepleon/NeverWork/search" method="get">      <span class="fieldwrap">
        <input type="text" name="q" value=""
          placeholder="Search source code&hellip;" /><button type="submit" class="minibutton"><span>Search</span></button>
      </span>
      <input type="hidden" id="lang-value" name="langOverride" value="" />
      <input type="hidden" id="start-value" name="start" value="" />
</form>  </li>

  </ul>

  <ul class="scope">
    <li class="switcher">

      <div class="context-menu-container js-menu-container">
        <a href="#"
           class="minibutton bigger switcher context-menu-button js-menu-target js-commitish-button btn-branch repo-tree"
           data-master-branch="master"
           data-ref="master">
          <span><span class="icon"></span><i>branch:</i> master</span>
        </a>

        <div class="context-pane commitish-context js-menu-content">
          <a href="javascript:;" class="close js-menu-close"></a>
          <div class="context-title">Switch Branches/Tags</div>
          <div class="context-body pane-selector commitish-selector js-filterable-commitishes">
            <div class="filterbar">
              <div class="placeholder-field js-placeholder-field">
                <label class="placeholder" for="context-commitish-filter-field" data-placeholder-mode="sticky">Filter branches/tags</label>
                <input type="text" id="context-commitish-filter-field" class="commitish-filter" />
              </div>

              <ul class="tabs">
                <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
              </ul>
            </div>

              <div class="commitish-item branch-commitish selector-item">
                <h4>
                    <a href="/stepleon/NeverWork/blob/master/NeverWork/predict.py" data-name="master" rel="nofollow">master</a>
                </h4>
              </div>


            <div class="no-results" style="display:none">Nothing to show</div>
          </div>
        </div><!-- /.commitish-context-context -->
      </div>

    </li>
  </ul>

  <ul class="subnav with-scope">
    
    <li><a href="/stepleon/NeverWork" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/stepleon/NeverWork/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/stepleon/NeverWork/branches" class="" highlight="repo_branches" rel="nofollow">Branches <span class="counter">1</span></a></li>
  </ul>

</div>

  
  
  


          

        </div><!-- /.repohead -->

        




  
  <p class="last-commit">Latest commit to the <strong>master</strong> branch</p>

<div class="commit commit-tease js-details-container">
  <p class="commit-title ">
      <a href="/stepleon/NeverWork/commit/7423e2a31bd6ffd7ed4879e65a7291dab858615d" class="message">make logo a link</a>
      
  </p>
  <div class="commit-meta">
    <a href="/stepleon/NeverWork/commit/7423e2a31bd6ffd7ed4879e65a7291dab858615d" class="sha-block">commit <span class="sha">7423e2a31b</span></a>

    <div class="authorship">
      <img class="gravatar" height="20" src="https://secure.gravatar.com/avatar/08232a56331bd9f50d57237e19020922?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="20" />
      <span class="author-name"><a href="/Salinon">Salinon</a></span>
      authored <time class="js-relative-date" datetime="2011-11-13T13:11:40-08:00" title="2011-11-13 13:11:40">November 13, 2011</time>

    </div>
  </div>
</div>


<!-- block_view_fragment_key: views4/v8/blob:v16:cbfe692cfa711a3f9f0ee0deca8e48ba -->
  <div id="slider">

    <div class="breadcrumb" data-path="NeverWork/predict.py/">
      <b><a href="/stepleon/NeverWork/tree/7423e2a31bd6ffd7ed4879e65a7291dab858615d" class="js-rewrite-sha">NeverWork</a></b> / <a href="/stepleon/NeverWork/tree/7423e2a31bd6ffd7ed4879e65a7291dab858615d/NeverWork" class="js-rewrite-sha">NeverWork</a> / predict.py       <span style="display:none" id="clippy_703" class="clippy-text">NeverWork/predict.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?1302750674?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_703&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?1302750674?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_703&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="NeverWork/predict.py/" data-permalink-url="/stepleon/NeverWork/blob/7423e2a31bd6ffd7ed4879e65a7291dab858615d/NeverWork/predict.py" data-title="NeverWork/predict.py at master from stepleon/NeverWork - GitHub" data-type="blob">
          <ul class="big-actions">
            <li><a class="file-edit-link minibutton js-rewrite-sha" href="/stepleon/NeverWork/edit/7423e2a31bd6ffd7ed4879e65a7291dab858615d/NeverWork/predict.py" data-method="post" rel="nofollow"><span>Edit this file</span></a></li>
          </ul>

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://a248.e.akamai.net/assets.github.com/images/icons/txt.png?1302750674" width="16" /></span>
                <span class="mode" title="File Mode">100644</span>
                  <span>64 lines (50 sloc)</span>
                <span>2.606 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/stepleon/NeverWork/raw/master/NeverWork/predict.py" id="raw-url">raw</a></li>
                  <li><a href="/stepleon/NeverWork/blame/master/NeverWork/predict.py">blame</a></li>
                <li><a href="/stepleon/NeverWork/commits/master/NeverWork/predict.py" rel="nofollow">history</a></li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">from</span> <span class="nn">__future__</span> <span class="kn">import</span> <span class="n">with_statement</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">google.appengine.ext</span> <span class="kn">import</span> <span class="n">webapp</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">google.appengine.ext.webapp.util</span> <span class="kn">import</span> <span class="n">run_wsgi_app</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">google.appengine.api</span> <span class="kn">import</span> <span class="n">app_identity</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">google.appengine.api</span> <span class="kn">import</span> <span class="n">files</span></div><div class='line' id='LC6'><span class="kn">from</span> <span class="nn">google.appengine.api</span> <span class="kn">import</span> <span class="n">urlfetch</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">simplejson</span> <span class="kn">as</span> <span class="nn">json</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="k">def</span> <span class="nf">getscores</span><span class="p">(</span><span class="n">out</span><span class="p">):</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">keys</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">values</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ind</span><span class="p">,</span> <span class="n">tup</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">out</span><span class="p">):</span></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">keys</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="n">ind</span><span class="p">][</span><span class="s">&quot;label&quot;</span><span class="p">])</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">values</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="n">ind</span><span class="p">][</span><span class="s">&quot;score&quot;</span><span class="p">])</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span><span class="p">(</span><span class="n">keys</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># return dict(zip(keys, values))</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="k">def</span> <span class="nf">predictCategory</span><span class="p">(</span><span class="n">responses</span><span class="p">):</span></div><div class='line' id='LC19'>&nbsp;&nbsp;<span class="n">scope</span> <span class="o">=</span> <span class="s">&quot;https://www.googleapis.com/auth/prediction&quot;</span></div><div class='line' id='LC20'>&nbsp;&nbsp;<span class="n">authorization_token</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">app_identity</span><span class="o">.</span><span class="n">get_access_token</span><span class="p">(</span><span class="n">scope</span><span class="p">)</span></div><div class='line' id='LC21'>&nbsp;&nbsp;<span class="n">payload</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;input&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s">&quot;csvInstance&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s">&quot;,&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">responses</span><span class="p">])]}})</span> <span class="c"># resp. in training range from 1..5</span></div><div class='line' id='LC22'>&nbsp;&nbsp;</div><div class='line' id='LC23'>&nbsp;&nbsp;<span class="n">api_key</span> <span class="o">=</span> <span class="s">&quot;AIzaSyD2ebps0y8lBONLnEjXl_JKJ9UjogZbZtg&quot;</span></div><div class='line' id='LC24'>&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="s">&#39;https://www.googleapis.com/prediction/v1.4/trainedmodels/nw_model/predict?key=&#39;</span> <span class="o">+</span> <span class="n">api_key</span>   </div><div class='line' id='LC25'>&nbsp;&nbsp;</div><div class='line' id='LC26'>&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">method</span> <span class="o">=</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">POST</span><span class="p">,</span> <span class="n">payload</span> <span class="o">=</span> <span class="n">payload</span><span class="p">,</span> <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;Content-Type&quot;</span><span class="p">:</span> <span class="s">&quot;application/json&quot;</span><span class="p">,</span> <span class="s">&quot;Authorization&quot;</span><span class="p">:</span> <span class="s">&quot;OAuth &quot;</span> <span class="o">+</span> <span class="n">authorization_token</span><span class="p">})</span></div><div class='line' id='LC27'>&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'>&nbsp;&nbsp;<span class="c"># job_scores = getscores(results[&quot;outputMulti&quot;])</span></div><div class='line' id='LC30'>&nbsp;&nbsp;<span class="c"># sl = [x for x in job_scores.iteritems()]</span></div><div class='line' id='LC31'>&nbsp;&nbsp;<span class="c"># sl.sort(key = lambda x: x[1])</span></div><div class='line' id='LC32'>&nbsp;&nbsp;<span class="c"># sl.reverse()</span></div><div class='line' id='LC33'>&nbsp;&nbsp;<span class="c"># for k, v in sl:</span></div><div class='line' id='LC34'>&nbsp;&nbsp;<span class="c">#     self.response.out.write(k)</span></div><div class='line' id='LC35'>&nbsp;&nbsp;<span class="c">#     self.response.out.write(v)</span></div><div class='line' id='LC36'>&nbsp;&nbsp;<span class="n">categories</span><span class="p">,</span> <span class="n">scores</span> <span class="o">=</span> <span class="n">getscores</span><span class="p">(</span><span class="n">results</span><span class="p">[</span><span class="s">&quot;outputMulti&quot;</span><span class="p">])</span></div><div class='line' id='LC37'>&nbsp;&nbsp;<span class="n">scores</span> <span class="o">=</span> <span class="p">[</span><span class="nb">float</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">scores</span><span class="p">]</span></div><div class='line' id='LC38'>&nbsp;&nbsp;<span class="c"># return((payload, response.content, results, categories, scores))</span></div><div class='line' id='LC39'>&nbsp;&nbsp;<span class="k">return</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">categories</span><span class="p">,</span> <span class="n">scores</span><span class="p">)</span></div><div class='line' id='LC40'>&nbsp;&nbsp;</div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'>&nbsp;&nbsp;</div><div class='line' id='LC43'>&nbsp;&nbsp;</div><div class='line' id='LC44'><span class="k">class</span> <span class="nc">Predict</span><span class="p">(</span><span class="n">webapp</span><span class="o">.</span><span class="n">RequestHandler</span><span class="p">):</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scope</span> <span class="o">=</span> <span class="s">&quot;https://www.googleapis.com/auth/prediction&quot;</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">authorization_token</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">app_identity</span><span class="o">.</span><span class="n">get_access_token</span><span class="p">(</span><span class="n">scope</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">payload</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="s">&quot;input&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s">&quot;csvInstance&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s">&quot;4,5,3,2,2,2,3,2,3,4,1,2,3,4,1,1,3,3,2,2,3,4,3,4,4&quot;</span><span class="p">]}})</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">api_key</span> <span class="o">=</span> <span class="s">&quot;AIzaSyD2ebps0y8lBONLnEjXl_JKJ9UjogZbZtg&quot;</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="s">&#39;https://www.googleapis.com/prediction/v1.4/trainedmodels/nw_model/predict?key=&#39;</span> <span class="o">+</span> <span class="n">api_key</span>   </div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">method</span> <span class="o">=</span> <span class="n">urlfetch</span><span class="o">.</span><span class="n">POST</span><span class="p">,</span> <span class="n">payload</span> <span class="o">=</span> <span class="n">payload</span><span class="p">,</span> <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;Content-Type&quot;</span><span class="p">:</span> <span class="s">&quot;application/json&quot;</span><span class="p">,</span> <span class="s">&quot;Authorization&quot;</span><span class="p">:</span> <span class="s">&quot;OAuth &quot;</span> <span class="o">+</span> <span class="n">authorization_token</span><span class="p">})</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">job_scores</span> <span class="o">=</span> <span class="n">getscores</span><span class="p">(</span><span class="n">results</span><span class="p">[</span><span class="s">&quot;outputMulti&quot;</span><span class="p">])</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sl</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">job_scores</span><span class="o">.</span><span class="n">iteritems</span><span class="p">()]</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sl</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sl</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">sl</span><span class="p">:</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">k</span><span class="p">)</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">v</span><span class="p">)</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading" style="display:none;" data-tree-list-url="/stepleon/NeverWork/tree-list/7423e2a31bd6ffd7ed4879e65a7291dab858615d" data-blob-url-prefix="/stepleon/NeverWork/blob/7423e2a31bd6ffd7ed4879e65a7291dab858615d">
  <img src="https://a248.e.akamai.net/assets.github.com/images/modules/ajax/big_spinner_336699.gif?1302750674" height="32" width="32">
</div>

      </div>
      <div class="context-overlay"></div>
    </div>


    <!-- footer -->
    <div id="footer" >
      
  <div class="upper_footer">
     <div class="container clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://enterprise.github.com/">GitHub Enterprise</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://get.gaug.es/">Gauges: Analyze web traffic</a></li>
         <li><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></li>
         <li><a href="https://gist.github.com">Gist: Code snippets</a></li>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://mobile.github.com/">Issues for iPhone</a></li>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Extras</h4>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="container clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
          <li><a href="https://github.com/site/terms">Terms of Service</a></li>
          <li><a href="https://github.com/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2012 <span id="_rrt" title="0.12452s from fe5.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspace_logo.png?v2" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

    </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selection as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selection as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selection from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div class="ajax-error-message">
      <p><span class="icon"></span> Something went wrong with that request. Please try again. <a href="javascript:;" class="ajax-error-dismiss">Dismiss</a></p>
    </div>

    
    
    
  </body>
</html>

